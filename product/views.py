from django.shortcuts import render
from .models import Popproduct, Topproduct, Product
from rest_framework.views import APIView
from .serializer import popproductserializer, topproductserializer, productserializer
from rest_framework.response import Response



class Popproductview(APIView):
  def get(self, request):
    getpop = Popproduct.objects.all()
    serializer = popproductserializer(getpop, many=True)
    return Response(serializer.data)
  


class topproductview(APIView):
  def get(self, request):
    gettop = Topproduct.objects.all()
    serializer = topproductserializer(gettop, many= True)
    return Response(serializer.data)
  

class productallview(APIView):
  def get(self, request):
    getall = Product.objects.all()
    serializer = productserializer(getall, many=True)
    return Response(serializer.data)


class allpview(APIView):
  def get(self, request):
    getall = Product.objects.all()
    serializer = productserializer(getall, many=True)
    return Response(serializer.data)

  
