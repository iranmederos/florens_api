from django.urls import path
from .views import *

urlpatterns = [
    path('get-last-report/',ShowLastReport.as_view(),name="GetLastReport"),
    path('list-attentions/',ShowAttentions.as_view(),name="ListAttentions"),
    path('create-report/',CreateReport.as_view(),name="ListLastReport"),
    path('create-health-check/',CreateHealthCheck.as_view(),name="ListAttentions"),
    path('create-attention/', CreateAttention.as_view(), name='create-atention'),
    path('create-order/', OrderCreate.as_view(), name='order_create'),
]

