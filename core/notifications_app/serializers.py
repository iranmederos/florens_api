from rest_framework.serializers import ModelSerializer
from .models import Notification

class NotificationSerializer(ModelSerializer):
    
    class Meta:
        model = Notification
        fields = '__all__'

class StateNotificationSerializer(ModelSerializer):

    class Meta:
        model = Notification
        fields = ['status'] 
        