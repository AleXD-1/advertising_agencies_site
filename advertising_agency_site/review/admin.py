from django.contrib import admin

from .models import Reviews


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'agency', 'client', 'publish_date', 'mark')
    fields = ('agency', 'client', 'review_text', 'mark')


admin.site.register(Reviews, ReviewAdmin)
