from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework import status
from .serializers import ReportSerializer, AttentionSerializer, StateAttentionSerializer, MedicalOrderSerializer
from .models import Report, AttentionOrder
from django.shortcuts import get_object_or_404
from django.utils import timezone
from patient_app.models import HealthCheck, MedicalOrder
from patient_app.serializers import HealthCheckSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from authentication.authentication_mixins import Authentication


# Create your views here.

#Muestra El ultimo reporte hecho a un paciente
class ShowLastReport(Authentication,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        patient_number = self.request.query_params.get('patient_number')
        last_report = Report.objects.filter(ine_patient=patient_number).last()
        if( last_report is not None):  
            listLastReportSerializer = ReportSerializer(last_report)
            return Response(listLastReportSerializer.data,status=status.HTTP_200_OK)

        return Response({"Message":"Error Patient Not Found"},status=status.HTTP_404_NOT_FOUND)

#registrar/crear atencion medica correspondiente a una orden medica

class CreateAttention(Authentication,CreateAPIView):
    serializer_class = AttentionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            num_order= request.data['num_order']
            update_order = MedicalOrder.objects.get(num_order=num_order)
            attetion_time= timezone.now()
            update_order.update_at = attetion_time 
            update_order.save() 

            return Response(
                {"message":"Se ha registrado la atencion correctamente"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": "Ocurrio un error al registrar la atencion: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

#Muestra todas las atenciones a realizar correspondientes a una orden medica
class ShowAttentions(Authentication,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        num_order = self.request.query_params.get('num_order')
        attentions = AttentionOrder.objects.filter(num_order=num_order)
        list_attentions = AttentionSerializer(attentions, many=True)

        if len(list_attentions.data)!=0:
            return Response(list_attentions.data, status=status.HTTP_200_OK)
        return Response({"Message":"No se encontraron atenciones para la orden medica"},status=status.HTTP_204_NO_CONTENT)



#registrar planes de cuidado del paciente
#ver modulo seriaizer
class OrderCreate(Authentication,CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class= MedicalOrderSerializer

#Crea un control de salud
class CreateHealthCheck(Authentication,CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = HealthCheckSerializer
    queryset = HealthCheck.objects.all()


class CreateReport(Authentication,CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ReportSerializer
    queryset = Report.objects.all()