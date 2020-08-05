from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CHOICE = [
    (0, "Unavailable"), (1, "Available")
    ]

class Product(models.Model):
    product_tag = models.CharField(max_length=255, default="P0001")
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField(default='aws.reqre.in/producs/image000001.jpg')
    status = models.BooleanField(choices=CHOICE)


    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    isbn = models.CharField(max_length=25)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField(default='aws.reqre.in/producs/image000001.jpg')
    status = models.BooleanField(choices=CHOICE)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, db_index=True)
    body = models.TextField()
    category = models.CharField(max_length=255)
    imageUrl = models.URLField(default='aws.reqre.in/articles/image000001.jpg')
    created_by = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
# class CovidCountry(models.Model):

