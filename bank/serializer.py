from bank.models import Order, Shippingaddress
from rest_framework import serializers




class orderserializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            '_id', 'totalprice', 'paymentmethod', 'product', 'user'
        )


class shippingserializer(serializers.ModelSerializer):
    class Meta:
        model = Shippingaddress
        fields = (
            'nocode', 'city', 'capital', 'address', 'user', 'id'
        )