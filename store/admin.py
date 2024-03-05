from django.db.models import Count
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count'] #the products_count is not in the models so we create a function

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


admin.site.register(models.OrderItem)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status', 'collection_title']
    list_editable = ['price']
    list_per_page = 10
    list_select_related = ['collection']
    

    def collection_title(self, product):
        return product.collection.title
    

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    inventory_status.short_description = 'Inventory Status'


@admin.register(models.Order)   
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'placed_at', 'customer') 


admin.site.register(models.Customer)


