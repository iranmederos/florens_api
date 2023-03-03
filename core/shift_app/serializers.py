from rest_framework.serializers import ModelSerializer
from .models import Shift

class ShiftSerializer(ModelSerializer):
    
    class Meta:
        model = Shift
        fields = '__all__'
        

class ShiftDateSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = ['entry_time', 'departure_time']
