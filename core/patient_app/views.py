from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import PatientSerializer, ClinicStorySerializer, HealthCheckSerializer, IntermentSerializer
from nurse_app.serializers import MedicalOrderSerializer
from .models import MedicalOrder, HealthCheck, ClinicStory, PatientUser, Interment
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication.authentication_mixins import Authentication

#vista que registrar paciente
class PatientCreate(Authentication,CreateAPIView):
    serializer_class = PatientSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(
                {"message":"Paciente creado exitosamente", "Numero de paciente creado": serializer.data['patient_number']},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": "Ocurrio un error al registrar paciente: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

#vista que actualiza el paciente
class UpdatePatient(Authentication,UpdateAPIView):
    serializer_class = PatientSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, patient_number):
        patient = get_object_or_404(PatientUser, patient_number=patient_number)
        serializer = self.get_serializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Paciente actualizado exitosamente"})

#listar planes de cuidados
class ShowCarePlan(Authentication,ListAPIView):
    serializer_class = MedicalOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_number = self.request.data.get('patient_number')
        planes_c= MedicalOrder.objects.filter(Q(id_cs__patient_number=patient_number) & Q(type='1')).all()
        if planes_c is None:
            raise serializers.ValidationError({"error": "No se encontraron ordenes medicas asociadas o no existe el paciente"})
        return planes_c
    
    def handle_exception(self, exc):
        if isinstance(exc, serializers.ValidationError):
            return Response(exc.detail, status=status.HTTP_400_BAD_REQUEST)
        return super().handle_exception(exc)

#Vista que devuelve los controles de salud del paciente
class ShowHealthCheck(Authentication,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patient = self.request.query_params.get('patient_number')
        list_health_check = HealthCheck.objects.filter(patient_number=patient)
        list_check = HealthCheckSerializer(list_health_check,many=True)
        
        if len(list_check.data)!=0:
            return Response(list_check.data, status=status.HTTP_200_OK)
        return Response({"Message":"El paciente no cuenta con controles de salud"},status=status.HTTP_404_NOT_FOUND)

#Vista que devuelve la ultima historia clinica de un paciente
class ShowClinicStory(Authentication,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        patient = self.request.query_params.get('patient_number')
        last_story = ClinicStory.objects.filter(patient_number=patient).last()
        if (last_story is not None):
            clinicStory = ClinicStorySerializer(last_story)
            return Response(clinicStory.data,status=status.HTTP_200_OK)
        return Response({"Message":"El paciente no cuenta con una historia clinica"},status=status.HTTP_404_NOT_FOUND) 


#Vista que devuelve las ordenes medicas activas
class ShowActiveOrders(Authentication,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(sefl,request):
        patient = request.data['patient_number']

        last_story = ClinicStory.objects.filter(patient_number=patient).last()
        clinicStory = ClinicStorySerializer(last_story)

        id_story = clinicStory.data.get('id_cs',None)

        try:
            medical_orden = MedicalOrder.objects.filter(id_cs=id_story, status=False)
            activity = MedicalOrderSerializer(medical_orden, many=True)
            if len(activity.data) == 0:
                return Response({"error":"No se encontraron ordenes medicas aasociadas"+str(Exception)}, status=status.HTTP_204_NO_CONTENT)
            
            return Response(activity.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error":"No se encontraron ordenes medicas aasociadas"+str(Exception)},status=status.HTTP_400_BAD_REQUEST)

#Vista que muestra el paciente 
class ShowPatient(Authentication,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        patient= request.data['patient_number']
        try:
            patient_data= PatientSerializer(PatientUser.objects.filter(patient_number=patient).get())
            return Response(patient_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_400_BAD_REQUEST)
        
#vista que crea las internaciones del paciente
class CreateInterment(Authentication,CreateAPIView):
    serializer_class = IntermentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(
                {"message":"Internacion creada exitosamente", "id del internacion": serializer.data['num_interment']},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": "error: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

#vista que actualiza las internaciones
class UpdateInterment(Authentication,UpdateAPIView):
    serializer_class = IntermentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, id_inter):
        interment = get_object_or_404(Interment, num_interment=id_inter)
        serializer = self.get_serializer(interment, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Internacion actualizada exitosamente"})
    
#vista que muestra los datos de internacion del paciente
class RetrieveInterment(Authentication,RetrieveAPIView):
    serializer_class = IntermentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, num_interment):
        interment = get_object_or_404(Interment, num_interment=num_interment)
        serializer = self.get_serializer(interment)
        return Response(serializer.data)