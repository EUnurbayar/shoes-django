from django.shortcuts import render
from .models import  Shoes, Brand
from .serializers import BrandSerializer, ShoesSerializer
from rest_framework import generics


# Create your views here.

class ShoesList(generics.ListCreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class ShoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
     