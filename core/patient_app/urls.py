from .views import PatientCreate, ShowCarePlan, ShowActiveOrders, ShowHealthCheck, ShowClinicStory, ShowPatient, CreateInterment, UpdateInterment, UpdatePatient, RetrieveInterment
from django.urls import path

urlpatterns = [
    path('create-patient/', PatientCreate.as_view(), name='patient_create'),
    path('update-patient/<str:patient_number>/', UpdatePatient().as_view(), name='update-patient'),
    path('show-care/', ShowCarePlan.as_view(), name='show_care_plan'),
    path('clinic_story/', ShowClinicStory.as_view(), name="ClinicStory"),
    path('health_check/', ShowHealthCheck.as_view(), name="HealthCheck"),
    path('activity_orden/', ShowActiveOrders.as_view(), name='Activity'),
    path('show-patient/', ShowPatient().as_view(), name='show-patient' ),
    path('create-interment/', CreateInterment().as_view(), name="create-interment"),
    path('update-interment/<str:id_inter>/', UpdateInterment().as_view(), name="update-interment"),
    path('retrieve-interment/<str:num_interment>/', RetrieveInterment.as_view(), name='retrieve-interment')
]
