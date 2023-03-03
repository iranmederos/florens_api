from django.db import models
from django.contrib.auth.models import AbstractUser
from shift_app.models import Shift

NURS_TYPE= (('1','Jefe de enfermera'),('2','Enfermera'))


class CustomUser(AbstractUser):
    user = models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    username =  models.CharField(max_length=50,null=True, blank=True,default=None)
    first_name = models.CharField(max_length=50,null=False, blank=False)
    last_name =  models.CharField(max_length=50,null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=False, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100,null=False, blank=False)   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
   
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"     


class Role(models.Model):
    name = models.CharField(max_length=10,null=False, blank=False,choices=NURS_TYPE,default=0)
    def __str__(self):
        return f"{self.name}"

class NursUser(CustomUser):

    nurs_number = models.CharField(max_length=5,null=False, blank=False,primary_key=True)
    professional_license = models.CharField(max_length=10,null=False, blank=False)
    category = models.CharField(max_length=20,null=False, blank=False)
    area = models.CharField(max_length=20,null=False, blank=False)
    state = models.CharField(max_length=10,null=False, blank=False)
    id_shift= models.ForeignKey(Shift, on_delete=models.CASCADE,null=True,default=None)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,default=None)

    class Meta:
        verbose_name = 'Nurse'
        verbose_name_plural = 'Nurses'




