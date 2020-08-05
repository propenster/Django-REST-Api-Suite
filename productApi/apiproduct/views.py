from .models import Product, Book, Article
from .serializers import ProductSerializer, BookSerializer, ArticleSerializer
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

class ListArticles(generics.ListCreateAPIView):
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer

class DetailArticle(generics.RetrieveUpdateDestroyAPIView):
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer        
        

