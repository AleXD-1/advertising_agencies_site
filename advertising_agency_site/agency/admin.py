from django.contrib import admin

from .models import Agencies, Services


class AgencyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'agency_name', 'region', 'city', 'address', 'post_index', 'work_phone', 'mobile_phone', 'web_site',
        'rating', 'user', 'services')
    fields = (
        'agency_name', 'description', 'region', 'city', 'address', 'post_index', 'work_phone', 'mobile_phone',
        'web_site', 'rating', 'logo', 'user', 'services')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    fields = ('title', 'description')


# class AgencyServiceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'agency', 'service')
#     fields = ('agency', 'service')


admin.site.register(Agencies, AgencyAdmin)
admin.site.register(Services, ServiceAdmin)
# admin.site.register(AgenciesServices, AgencyServiceAdmin)
