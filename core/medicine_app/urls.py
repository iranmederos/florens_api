from django.urls import path
from .views import *

urlpatterns = [
    path('list-pending-medical-orders/',ListAllPendingMedicalOrders.as_view(),name="list-pending"),
    path('list-pending-medical-cards/',ListAllPendingMedicalCards.as_view(),name="list-pending"),
    path('get-last-medical-card-completed/',LastMedicalCardCompleted.as_view(),name="get-last-administered"),
    path('get-all-medical-cards-completed/',ListAllMedicalOrdercompleted.as_view(),name="get-all-administered"),
    path('register-medical-card/<int:pk>/',RegisterMedicalCard.as_view(),name="register-order-medication"),
]

