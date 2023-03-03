from django.contrib import admin
from .models import Shift
# Register your models here.

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id_shift', 'entry_time', 'departure_time')

admin.site.register(Shift, ShiftAdmin)