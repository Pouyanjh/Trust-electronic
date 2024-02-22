from rest_framework import generics
from .models import dasteha
from .serializer import dasterserializer


class DasteListView(generics.ListCreateAPIView):
  queryset = dasteha.objects.all()
  serializer_class = dasterserializer
