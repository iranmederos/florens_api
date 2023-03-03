from django.db import models
from authentication.models import NursUser
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

ORDER_TYPE= (('1','Plan de cuidados'),('2','Tarjeta Médica'))
GENERO= (('M','Masculino'),('F','Femenino'),('X','No binario'))

class ViaChoice(models.Model):
    via_type= models.CharField(max_length=50)


class PatientUser(models.Model):
    patient_number= models.CharField(max_length=5, primary_key=True, null=False, unique=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    sex= models.CharField(max_length=30, choices=GENERO)
    age= models.IntegerField(validators=[MinValueValidator(1)])
    birthday= models.DateTimeField()
    address: models.CharField(max_length=30)
    precautions= models.CharField(max_length=300)
    date_adminission= models.DateTimeField()
    proccedings= models.CharField(max_length=10)


class HealthCheck(models.Model):
    control_number= models.CharField(primary_key=True, max_length=5, null=False, unique=True)
    pressure= models.FloatField(validators=[MinValueValidator(1)])
    oxygen= models.IntegerField(validators=[MinValueValidator(1)])
    pulse= models.IntegerField(validators=[MinValueValidator(1)])
    weigth= models.FloatField(validators=[MinValueValidator(1)])
    patient_number= models.ForeignKey(PatientUser, on_delete=models.CASCADE)



class ClinicStory(models.Model):
    id_cs= models.CharField(max_length=100, primary_key=True, null=False, unique=True)
    date= models.DateTimeField()
    name_doctor= models.CharField(max_length=100)
    archive= models.CharField(max_length=120)
    patient_number= models.ForeignKey(PatientUser, on_delete=models.DO_NOTHING)


class MedicalOrder(models.Model):
    num_order= models.CharField(max_length=5,primary_key=True, null=False, unique=True)
    type= models.CharField(max_length=30, choices=ORDER_TYPE)
    start_date= models.DateTimeField()
    end_date= models.DateTimeField()
    description= models.CharField(max_length=100)
    created_by = models.CharField(max_length=100,blank=True, null=True)
    status=models.BooleanField(default=False)
    atettions= models.IntegerField(validators=[MinValueValidator(0)])
    ine_nurs=models.ForeignKey(NursUser, on_delete=models.DO_NOTHING)
    id_cs=models.ForeignKey(ClinicStory, on_delete=models.DO_NOTHING)
    update_at = models.DateTimeField(auto_now=True,blank=True)

    def clean(self) -> None:
        if self.start_date > self.end_date:
            raise ValidationError('La fecha de fin no puede ser anterior a la de entrada')


class Interment(models.Model):
    num_interment= models.CharField(max_length=5, primary_key=True, null=False, unique=True)
    date_admision= models.DateField()
    egress_date= models.DateField(null=True, blank=True)
    living_room= models.CharField(max_length=20)
    bed_number=models.CharField(max_length=5)
    condition=models.CharField(max_length=10)
    patient_number=models.ForeignKey(PatientUser, on_delete=models.CASCADE)
    diagnosis= models.CharField(max_length=20)

    def clean(self) -> None:
        if self.date_admision > self.egress_date:
            raise ValidationError('La fecha de egreso no puede ser anterior a la de admision')