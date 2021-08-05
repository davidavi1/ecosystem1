from django.contrib import admin
from .models import FeedBackModel


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'subject', 'text', 'date']
    list_display_links = ['name', 'last_name', 'subject', 'text', 'date']


admin.site.register(FeedBackModel, FeedBackAdmin)
