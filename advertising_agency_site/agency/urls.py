from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('agency/<int:agency_id>', view_agency, name='agency'),
    path('service/<int:service_id>/', get_service, name='service'),
    path('profile/', get_profile, name='profile'),
    path('create_agency/', create_agency, name='create_agency')
]
