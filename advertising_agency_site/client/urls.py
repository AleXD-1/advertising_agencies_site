from django.urls import path

from .views import *

urlpatterns = [
    path('create_client', create_client_profile, name='create_client_profile'),
    path('client_profile', get_client_profile, name='client_profile'),
]
