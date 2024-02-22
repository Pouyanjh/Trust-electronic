from rest_framework import serializers
from .models import Popproduct, Product, Topproduct

class popproductserializer(serializers.ModelSerializer):

  class Meta:
    model = Popproduct
    fields = (
      'title', 'id', 'image', 'description', 'price'
    )
    

class topproductserializer(serializers.ModelSerializer):

  class Meta:
    model = Topproduct
    fields = (
      'title', 'id', 'image', 'description', 'price'
    )


class productserializer(serializers.ModelSerializer):

  class Meta:
    model = Product
    fields = (
      'title', 'id', 'image', 'description', 'price'
    )

