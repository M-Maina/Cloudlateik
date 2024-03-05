from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.

def hello(request):
    try:
      product = Product.objects.all()
    except ObjectDoesNotExist:
       pass
    return render(request, "hello.html", {'name':'wamah'})


