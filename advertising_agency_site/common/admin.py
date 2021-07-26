from django.contrib import admin

from .models import Cities, Regions, Profiles


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city',)
    fields = ('city',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'region',)
    fields = ('region',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_type', 'created_date')
    fields = ('profile_type',)


admin.site.register(Cities, CityAdmin)
admin.site.register(Regions, RegionAdmin)
admin.site.register(Profiles, ProfileAdmin)
