from django.shortcuts import get_list_or_404
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from patient_app.serializers import RegisterMedicalOrderSerializer
from patient_app.models import MedicalOrder
from nurse_app.serializers import MedicalOrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from authentication.authentication_mixins import Authentication

# Create your views here.

#Lista todo los medicamentos pendientes de un paciente
class ListAllPendingMedicalOrders(Authentication,ListAPIView):
    serializer_class = MedicalOrderSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = MedicalOrder.objects.filter(status=0)   
    def get_queryset(self):
        queryset = self.queryset.all()
        patient_number = self.request.query_params.get('patient_number',None)
        if patient_number is not None and queryset.count():
            queryset = get_list_or_404(queryset, id_cs__patient_number=patient_number)
        return queryset


class ListAllPendingMedicalCards(Authentication,ListAPIView):
    serializer_class = MedicalOrderSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = MedicalOrder.objects.filter(status=0)   
    def get_queryset(self):
        queryset = self.queryset.all()
        patient_number = self.request.query_params.get('patient_number',None)
        if patient_number is not None and queryset.count():
            queryset = get_list_or_404(queryset, Q(id_cs__patient_number=patient_number)& Q(type=2))
        return queryset
    
#Obtiene el ultimo medicamento aplicado a un paciente
class LastMedicalCardCompleted(Authentication,APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        patient_number = self.request.query_params.get('patient_number',None)
        if patient_number is not None:
            queryset = MedicalOrder.objects.filter(Q(status=1) & Q(id_cs__patient_number=patient_number)).order_by('update_at').last()
            if queryset is not None:
                data = MedicalOrderSerializer(queryset).data
                code = status.HTTP_200_OK
            else:
                data = {"Error":"Order Not found"}
                code = status.HTTP_404_NOT_FOUND   
        else:
            data = {"Error":"Null"}
            code = status.HTTP_404_NOT_FOUND
        return Response(data,status=code)

class ListAllMedicalOrdercompleted(Authentication,ListAPIView):
    serializer_class = MedicalOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = MedicalOrder.objects.filter(status=1)   
    def get_queryset(self):
        queryset = self.queryset.all()
        patient_number = self.request.query_params.get('patient_number',None)
        if patient_number is not None and queryset.count():
            queryset = get_list_or_404(queryset, id_cs__patient_number=patient_number)
        return queryset


class RegisterMedicalCard(Authentication,UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = RegisterMedicalOrderSerializer
    queryset = MedicalOrder.objects.all()