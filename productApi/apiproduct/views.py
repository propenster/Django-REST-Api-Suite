from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics


# Create your views here.

class ListProduct(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

        

