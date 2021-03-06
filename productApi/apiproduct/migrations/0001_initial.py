# Generated by Django 3.1 on 2020-08-05 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('available', models.BooleanField(choices=[(0, 'Unavailable'), (1, 'Available')])),
                ('description', models.TextField()),
            ],
        ),
    ]
