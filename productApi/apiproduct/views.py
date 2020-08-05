from .models import Product, Book
from .serializers import ProductSerializer, BookSerializer
from rest_framework import generics


# Create your views here.

class ListProduct(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

class ListBooks(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer        

        

