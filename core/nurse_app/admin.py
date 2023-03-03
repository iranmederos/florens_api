from django.contrib import admin
from .models import Report, InputRequest, AttentionOrder
# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_number','description')

class InputAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'date', 'ine_nurs','note')

class AttentionAdmin(admin.ModelAdmin):
    list_display = ('num_attention','status', 'num_order')

admin.site.register(Report, ReportAdmin)
admin.site.register(InputRequest, InputAdmin)
admin.site.register(AttentionOrder, AttentionAdmin)