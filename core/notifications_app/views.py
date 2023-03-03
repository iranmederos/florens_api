from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from .serializers import NotificationSerializer, StateNotificationSerializer
from .models import Notification
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from authentication.authentication_mixins import Authentication
import datetime


# Create your views here.

#Metodo para crear una notificacion
class CreateNotification(Authentication,CreateAPIView):
    serializer_class = NotificationSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(
                {"message":"Notificacion creada exitosamente"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": "Ocurrio un error al crear la notificacion: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

#Vista que devuelve las notificaciones que se encuentran en un intervalo de una hora
#con respecto al tiempo actual
class ShowNotification(Authentication,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ine_nurs = request.query_params.get('ine_nurs')

        today = datetime.datetime.now()
        next_time = today + datetime.timedelta(hours=1)

        list_noti = Notification.objects.filter(Q(num_order__ine_nurs=ine_nurs) & Q(status=False) &  Q(initial_time__gte=today) & Q(initial_time__lte=next_time)).all()
        notifications = NotificationSerializer(list_noti, many = True)

        if len(notifications.data) != 0:
            return Response(notifications.data,status=status.HTTP_200_OK)
        return Response({"Message":"Por ahora no tienes tareas pendientes"},status=status.HTTP_204_NO_CONTENT)


#Metodo para modificar el estado de una notificacion
class StatusNotification(Authentication,UpdateAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = StateNotificationSerializer
    queryset = Notification.objects.all()