from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Product
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
