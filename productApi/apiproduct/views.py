from .models import Product, Book, Article
from .serializers import ProductSerializer, BookSerializer, ArticleSerializer
from rest_framework import generics
from rest_framework import permissions


# Create your views here.

class ListProduct(generics.ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticated,)
        queryset = Product.objects.all()
        serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (permissions.IsAuthenticated,)
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

class ListBooks(generics.ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticated,)
        queryset = Book.objects.all()
        serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (permissions.IsAuthenticated,)
        queryset = Book.objects.all()
        serializer_class = BookSerializer        

class ListArticles(generics.ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticated,)
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer

class DetailArticle(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (permissions.IsAuthenticated,)
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer        
        

