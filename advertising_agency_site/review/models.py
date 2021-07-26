from django.db import models
from agency.models import Agencies
from client.models import Clients


class Reviews(models.Model):
    mark_types = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    agency = models.ForeignKey(Agencies, on_delete=models.DO_NOTHING, verbose_name='Agency')
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, verbose_name='Client')
    review_text = models.TextField(blank=True, verbose_name='Review text')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of publication')
    mark = models.IntegerField(max_length=1, choices=mark_types, verbose_name='Mark', default=3)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
