# Generated by Django 3.1 on 2020-08-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiproduct', '0003_product_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.CharField(default='P0001', max_length=255),
        ),
    ]
