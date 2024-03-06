from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializers


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid()
        serializer.validated_data
        return Response('ok')
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    


@api_view()
def Product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializers(product)
    return Response(request, serializer.data)
   
    
    
    