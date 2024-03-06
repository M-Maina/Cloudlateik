from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:id>/', views.Product_detail, name='product_detail'),
    
]
