from django.contrib import admin
from .models import *

class Registered_Case(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')

admin.site.register(Case, Registered_Case)
