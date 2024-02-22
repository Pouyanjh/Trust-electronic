from rest_framework import serializers
from .models import zirdaste, dasteha

class zirdasteserializer(serializers.ModelSerializer):

  class Meta:
    model = zirdaste
    fields = (
      'name', 'id'
    )

class dasterserializer(serializers.ModelSerializer):
  zirdasteha = zirdasteserializer(many=True, read_only=True)


  class Meta:
    model = dasteha
    fields = (
      'id', 'name', 'zirdasteha'
    )
