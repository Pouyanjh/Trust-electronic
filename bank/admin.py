from django.contrib import admin

from bank.models import Order, zibal, Shippingaddress


@admin.register(Order)
class orderadmin(admin.ModelAdmin):
    list_display = ['_id', 'totalprice']
    search_fields = ['_id']

@admin.register(zibal)
class zibaladmin(admin.ModelAdmin):
    list_display = ['Condition', 'lastStatus', 'transId']


@admin.register(Shippingaddress)

class shippingadmin(admin.ModelAdmin):
    list_display = ['nocode', 'address', 'city', 'capital', 'id', 'user', 'seen']
    search_fields = ['user']