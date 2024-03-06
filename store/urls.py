from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list),
    path('product/<int:id>/', views.Product_detail),
    
]
