from django.db import models
from patient_app.models import MedicalOrder
# Create your models here.

class Medicine(models.Model):
    drug_code = models.CharField(max_length=5,primary_key=True,unique=True,null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    mechanism_action = models.CharField(max_length=300,null=False,blank=False)
    mode_administration = models.CharField(max_length=300,null=False,blank=False)
    adverse_reactions = models.CharField(max_length=300,null=False,blank=False)
    batch = models.CharField(max_length=10,null=False,blank=False)
    brand = models.CharField(max_length=20,null=False,blank=False)

class Order_Medicine(models.Model):
    num_OM = models.CharField(max_length=5,primary_key=True,unique=True,null=False,blank=False)
    via = models.CharField(max_length=10,null=False,blank=False)
    dose = models.IntegerField(null=False,blank=False)
    frecuency = models.IntegerField(null=False,blank=False)
    drug_code = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    num_order = models.ForeignKey(MedicalOrder, on_delete=models.CASCADE)
    