from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

class Shift(models.Model):
    id_shift= models.CharField(primary_key=True, max_length=10, null=False, unique=True)
    entry_time= models.DateTimeField()
    departure_time= models.DateTimeField()
    number_nurses= models.IntegerField(validators=[MinValueValidator(1)])

    def clean(self) -> None:
        if self.entry_time > self.departure_time:
            raise ValidationError('La fecha de fin del turno no puede ser anterior a la de entrada')
    