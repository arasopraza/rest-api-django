from store.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'category', 'price', 'stock', 'location', 'is_available']