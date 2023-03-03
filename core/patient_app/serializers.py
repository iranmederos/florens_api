from rest_framework.serializers import ModelSerializer
from .models import PatientUser, MedicalOrder, ClinicStory, HealthCheck, Interment

class PatientSerializer(ModelSerializer):
    
    class Meta:
        model = PatientUser
        fields = '__all__'
        

class RegisterMedicalOrderSerializer(ModelSerializer):
    class Meta:
        model = MedicalOrder
        fields = ['description','status',]

class HealthCheckSerializer(ModelSerializer):
    
    class Meta:
        model = HealthCheck
        fields = '__all__'



class ClinicStorySerializer(ModelSerializer):
    
    class Meta:
        model = ClinicStory
        fields = '__all__'

class IntermentSerializer(ModelSerializer):

    class Meta:
        model = Interment
        fields= '__all__'