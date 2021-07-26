from django.contrib import admin

from .models import Clients


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'birth_date', 'user')
    fields = ('phone', 'birth_date', 'user')


admin.site.register(Clients, ClientAdmin)
