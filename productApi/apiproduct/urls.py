from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ListProduct.as_view()),
    path('products/<int:pk>/', views.DetailProduct.as_view()),
    path('books', views.ListBooks.as_view()),
    path('books/<int:pk>/', views.DetailBook.as_view()),
    path('articles', views.ListArticles.as_view()),
    path('articles/<int:pk>/', views.DetailArticle.as_view()),

]