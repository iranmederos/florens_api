from django.db import models
from patient_app.models import MedicalOrder

# Create your models here.

class Notification(models.Model):
    initial_time= models.DateTimeField()
    time_interval= models.DateTimeField() 
    repetitions= models.IntegerField()
    status= models.BooleanField(default=False)
    tittle = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    num_order= models.ForeignKey(MedicalOrder, on_delete=models.DO_NOTHING)
