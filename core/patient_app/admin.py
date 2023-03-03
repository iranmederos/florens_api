from django.contrib import admin
from .models import PatientUser, HealthCheck, MedicalOrder, ClinicStory, ViaChoice, Interment
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_number', 'first_name')

class HealthAdmin(admin.ModelAdmin):
    list_display = ('control_number', 'patient_number')

class MedicalOrderAdmin(admin.ModelAdmin):
    list_display = ('num_order', 'start_date', 'ine_nurs','id_cs','update_at')

class ClinicAdmin(admin.ModelAdmin):
    list_display = ('id_cs', 'date', 'name_doctor','archive')

class IntermentAdmin(admin.ModelAdmin):
    list_display=('num_interment','date_admision','patient_number')
    


admin.site.register(PatientUser, PatientAdmin)
admin.site.register(HealthCheck, HealthAdmin)
admin.site.register(MedicalOrder, MedicalOrderAdmin)
admin.site.register(ClinicStory, ClinicAdmin)
admin.site.register(ViaChoice)
admin.site.register(Interment, IntermentAdmin)