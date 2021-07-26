from django.db import models
from django.contrib.auth.models import User


class Regions(models.Model):
    region = models.CharField(max_length=100, verbose_name='Region')

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        ordering = ['region']


class Cities(models.Model):
    city = models.CharField(max_length=50, verbose_name='City')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['city']


class Profiles(models.Model):
    profile_types = [
        ('AG', 'Agency'),
        ('CL', 'Client')
    ]

    created_date = models.DateField(auto_now_add=True)
    profile_type = models.CharField(max_length=2, choices=profile_types)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
