from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,CreateAPIView
from .serializers import RegisterSerializer,NursUserSerializer
from authentication.models import  NursUser
from rest_framework.permissions import AllowAny

from django.utils import timezone

from .authentication import token_expire_handler, expires_in

class Register(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = self.get_serializer(data=request.data) 
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            try:
                user = serializer.save()
                Token.objects.create(user = user)
                data = {'code': 201, 'msg': 'Usuario creado'}
                code = status.HTTP_201_CREATED
            except Exception as err:
                    print(err)
                    data = {'code': 400, 'msg': 'error al crear usuario o ya existe'}
                    code = status.HTTP_400_BAD_REQUEST    
        return Response(data, status = code)         


class AddNurse(CreateAPIView):
    serializer_class = NursUserSerializer
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        user_req = request.data['user_nurs']
        serializer = self.get_serializer(data=request.data) 
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            try:
                user = NursUser.objects.get(nurs_number=user_req)
                
                if int(str(user.role)) == 1:
                    password_hash = make_password(self.request.data['password'])
                    self.request.data['password'] = password_hash
                    return self.create(request, *args, **kwargs)
                else:
                    data = {'code': 400, 'msg': 'No es un enfermero en jefe'}
                    code = status.HTTP_400_BAD_REQUEST
                    return Response(data, status = code) 
            
            except Exception as err:
                    print(err)
                    data = {'code': 400, 'msg': 'No existe el usuario'}
                    code = status.HTTP_400_BAD_REQUEST    
        return Response(data, status = code) 



class Login(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        email = email.replace(" ", "")
        
        try:
            user = NursUser.objects.get(email = email)
            if str(user.role) == "2":
                now = timezone.now()

                entry = user.id_shift.entry_time
                departure = user.id_shift.departure_time

                if entry <= now <= departure:
                    hash_pass = user.password 
                    verify_pass = check_password(password, hash_pass)
                else:
                    return JsonResponse({'error': 'No estas en horario Laboral'}, status=400)
                
            hash_pass = user.password 
            verify_pass = check_password(password, hash_pass)
        except Exception as e:
            print(e)
            verify_pass = False
       
        
        if verify_pass:
            try:
                token , _ = Token.objects.get_or_create(user = user)
                is_expired = token_expire_handler(token)
                user_serialized = RegisterSerializer(user)
                
            except Token.DoesNotExist:
                token = Token.objects.create(user = user)
            data = {
                'user': user_serialized.data, 
                'expires_in': expires_in(token),
                'token': token.key
            }
            code = status.HTTP_202_ACCEPTED

            
        else:    
            data = {'code': 401, 'msg': 'Credenciales incorrectas'}
            code = status.HTTP_401_UNAUTHORIZED
        
        return Response(data, status = code)
            

class Logout(APIView):
    permission_classes = [AllowAny] 
    
    def post(self, request):
        email = request.data['email']
        try:
            user = NursUser.objects.get(email = email)
            token = Token.objects.get(user = user)
            token.delete()
            data = {'code': 200, 'msg': 'Sesión cerrada'}
            code = status.HTTP_200_OK
        except:
            data = {'code': 401, 'msg': 'Credenciales incorrectas'}
            code = status.HTTP_401_UNAUTHORIZED
        return Response(data, status = code)

