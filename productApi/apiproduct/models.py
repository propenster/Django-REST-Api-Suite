from django.db import models
# Create your models here.

CHOICE = [(0, "Unavailable"), (1, "Available")]

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


