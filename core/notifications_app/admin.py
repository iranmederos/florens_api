from django.contrib import admin
from .models import Notification
# Register your models here.

class NotifiAdmin(admin.ModelAdmin):
    list_display=('id', 'initial_time', 'status')

admin.site.register(Notification, NotifiAdmin)