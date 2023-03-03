from .views import ShowNurseForShift, CreateShift, UpdateShift, DeleteShift, RetrieveShiftDate
from django.urls import path

urlpatterns = [
    path('show-nurses-shift/', ShowNurseForShift.as_view(), name='show-nurses-shift'),
    path('create-shift/', CreateShift.as_view(), name='create-shift'),
    path('update-shift/<str:id_shift>/', UpdateShift.as_view(), name='update-shift'),
    path('delete-shift/<str:id_shift>/', DeleteShift.as_view(), name='delete-shift'),
    path('retrieve-shift-date/<str:id_shift>/', RetrieveShiftDate.as_view(), name='retrieve-shift-date')
]
