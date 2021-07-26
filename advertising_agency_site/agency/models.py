from django.db import models
from common.models import Regions, Cities
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='Service')
    description = models.TextField(blank=True, verbose_name='Service description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_id': self.pk})


class Agencies(models.Model):
    agency_name = models.CharField(max_length=100, verbose_name='Name of agency', blank=True)
    description = models.TextField(verbose_name='Description of the agency', blank=True)
    region = models.ForeignKey(Regions, on_delete=models.DO_NOTHING, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.DO_NOTHING, blank=True)
    address = models.CharField(max_length=55, verbose_name='Address of the agency', blank=True)
    post_index = models.IntegerField(max_length=5, verbose_name='Post index', default=0, blank=True)
    work_phone = models.CharField(max_length=20, verbose_name='Work phone', blank=True)
    mobile_phone = models.CharField(max_length=20, verbose_name='Mobile phone', blank=True)
    web_site = models.URLField(verbose_name='Site', blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Rating', default=0, blank=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Logo', blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    services = models.ForeignKey(Services, on_delete=models.PROTECT, default=None, blank=True)

    def __str__(self):
        return self.agency_name

    class Meta:
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

    def get_absolute_url(self):
        return reverse('agency', kwargs={'agency_id': self.pk})
