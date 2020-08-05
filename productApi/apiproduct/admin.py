from django.contrib import admin
from .models import Product, Book, Article
# Register your models here.

admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Article)