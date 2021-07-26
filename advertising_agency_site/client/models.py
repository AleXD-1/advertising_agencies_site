from django.db import models
from django.contrib.auth.models import User


class Clients(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Phone', blank=True)
    birth_date = models.DateField(verbose_name='Birth date', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
