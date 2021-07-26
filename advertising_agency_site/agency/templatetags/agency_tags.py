from django import template
from django.db.models import Count, F

from agency.models import Services

register = template.Library()


@register.inclusion_tag('agency/list_services.html')
def show_services():
    services = Services.objects.annotate(cnt=Count('agencies'))
    return {'services': services}
