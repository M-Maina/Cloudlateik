from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializers(serializers.Serializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializers(serializers.Serializer):
    class Meta:
        model =Product
        fields =['id', 'title', 'unit_price', 'collection']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)

