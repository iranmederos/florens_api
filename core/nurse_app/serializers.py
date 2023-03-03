from rest_framework.serializers import ModelSerializer
from .models import Report, InputRequest, AttentionOrder
from .models import Report, InputRequest
from patient_app.models import MedicalOrder
from rest_framework import serializers

class ReportSerializer(ModelSerializer):
    
    class Meta:
        model = Report
        fields = '__all__'
        
class InputRequestSerializer(ModelSerializer):
    
    class Meta:
        model = InputRequest
        fields = '__all__'

class AttentionSerializer(ModelSerializer):

    class Meta:
        model = AttentionOrder
        fields = '__all__'

class StateAttentionSerializer(ModelSerializer):

    class Meta:
        model = AttentionOrder
        fields = ('completed.by','note','status')
class MedicalOrderSerializer(ModelSerializer):
    
    class Meta:
        model = MedicalOrder
        fields = '__all__'

    def to_internal_value(self, data):
        type = data.get('type')
        if type == '1':
            data.pop('via')
            data.pop('dose')
            data.pop('drug_code')
        elif type == '2':
            pass
        else:
            raise serializers.ValidationError({'type': 'Valor inválido'})
        return super().to_internal_value(data)
