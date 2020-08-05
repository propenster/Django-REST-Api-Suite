from django.db import models
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


# class CovidCountry(models.Model):



