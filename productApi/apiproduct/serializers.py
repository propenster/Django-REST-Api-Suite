from rest_framework import serializers
from .models import Product, Book

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

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'category',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',

        )
        model = Book