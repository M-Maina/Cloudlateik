from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers



def Product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializers(product)
    return Response(request, serializer.data)