from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'price',
            'quantity',
            'description',
            'imageUrl',
            'status',

        )
        model = Product