from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from authentication.models import CustomUser, NursUser

from django.core.validators import RegexValidator,MinLengthValidator

from django.contrib.auth.hashers import make_password
class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class NursUserSerializer(ModelSerializer):
    
    class Meta:
        model = NursUser
        exclude = ('user_permissions','groups','date_joined','is_active','is_staff','last_login','customuser_ptr','is_superuser')

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W_])',
                message='El password debe tener al menos un número, una letra mayúscula, una letra minúscula y un signo de puntuación',
            ),
            MinLengthValidator(13, 'El password debe tener al menos 13 caracteres'),
        ]
    )

    class Meta:
        model = NursUser
        fields = ('nurs_number', 'first_name', 'last_name', 'phone_number', 'email', 'password','role')

    def create(self, validated_data):
        hash_password = make_password(validated_data['password'])  

        user = NursUser.objects.create(
            nurs_number = validated_data['nurs_number'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_number = validated_data['phone_number'],
            email = validated_data['email'],
            password = hash_password,
            role = validated_data['role']
        )
        return user