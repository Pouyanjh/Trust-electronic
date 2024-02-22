from django.contrib import admin
from .models import zirdaste, dasteha

@admin.register(dasteha)

class dasteadmin(admin.ModelAdmin):
  list_display = ['name', 'id']

@admin.register(zirdaste)

class zirdasteadmin(admin.ModelAdmin):
  list_display = ['name', 'id']
