from django.contrib import admin
from .models import Product, Popproduct, Topproduct


@admin.register(Product)

class productadmin(admin.ModelAdmin):
  list_display = ['title', 'id', 'price']



@admin.register(Topproduct)

class topproductadmin(admin.ModelAdmin):
  list_display = ['title', 'id', 'price']



@admin.register(Popproduct)

class popproductadmin(admin.ModelAdmin):
  list_display = ['title', 'id', 'price']


