from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import CustomUser, NursUser,Role

class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ("user","first_name", "last_name", "email")

class NursUserAdmin(admin.ModelAdmin):
    list_display = ("user","first_name", "last_name", "email")
    fieldsets = (
      ('Personal info', {
          'fields': ('first_name','last_name','phone_number','email','password')
      }),
      ('Professional info', {
          'fields': ('nurs_number','professional_license','category','area','state','id_shift','role')
      }),
   )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(NursUser,NursUserAdmin)
admin.site.register(Role)
