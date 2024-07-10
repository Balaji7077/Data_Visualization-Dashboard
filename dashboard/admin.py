from django.contrib import admin
from dashboard.models import *

# Register your models here.

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('topic', 'country', 'year', 'intensity', 'likelihood', 'relevance', 'region', 'city')
