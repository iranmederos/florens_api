from .views import *
from django.urls import path

urlpatterns = [
    path('create-notification/', CreateNotification.as_view(), name='create_notification'),
    path('show-notification/', ShowNotification.as_view(), name='show_notification'),
    path('status-notification/<int:pk>', StatusNotification.as_view(), name='status-notification')
]