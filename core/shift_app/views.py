from django.shortcuts import render
from authentication.models import NursUser
from .models import Shift
from .serializers import ShiftSerializer, ShiftDateSerializer
from authentication.serializers import NursUserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from django.db.models import Q
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from authentication.authentication_mixins import Authentication

# Create your views here.

class ShowNurseForShift(Authentication,ListAPIView):
    serializer_class= NursUserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_shift_request= self.request.data.get('id_shift')
        nursers= NursUser.objects.filter(Q(id_shift=id_shift_request)).all()
        if not nursers:
            raise serializers.ValidationError({"error": "No se encontraron enfermeras en el turno"})
        return nursers
    
    def handle_exception(self, exc):
        if isinstance(exc, serializers.ValidationError):
            return Response(exc.detail, status=status.HTTP_400_BAD_REQUEST)
        return super().handle_exception(exc)


class CreateShift(Authentication,CreateAPIView):
    serializer_class = ShiftSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(
                {"message":"Turno creado exitosamente", "id del turno": serializer.data['id_shift']},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": "Ocurrio un error al crear el turno: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

class DeleteShift(Authentication,DestroyAPIView):
    serializer_class = ShiftSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, id_shift):
        shift = get_object_or_404(Shift, id_shift=id_shift)
        shift.delete()
        return Response({"message": "Turno eliminado exitosamente"})


class UpdateShift(Authentication,UpdateAPIView):
    serializer_class = ShiftSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, id_shift):
        shift = get_object_or_404(Shift, id_shift=id_shift)
        serializer = self.get_serializer(shift, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Turno actualizado exitosamente"})


class RetrieveShiftDate(Authentication,RetrieveAPIView):
    serializer_class = ShiftDateSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, id_shift):
        shift = get_object_or_404(Shift, id_shift=id_shift)
        serializer = self.get_serializer(shift)
        return Response(serializer.data)
