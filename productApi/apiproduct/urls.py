from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProduct.as_view()),
    path('<int:pk>/', views.DetailProduct.as_view()),
]