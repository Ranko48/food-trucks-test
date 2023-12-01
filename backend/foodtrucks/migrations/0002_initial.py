# Generated by Django 4.2.7 on 2023-12-01 13:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodtrucks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('locationid', models.IntegerField(primary_key=True, serialize=False)),
                ('Applicant', models.CharField(max_length=255)),
                ('FacilityType', models.CharField(max_length=255)),
                ('cnn', models.IntegerField()),
                ('LocationDescription', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('blocklot', models.CharField(max_length=255)),
                ('block', models.CharField(max_length=255)),
                ('lot', models.CharField(max_length=255)),
                ('permit', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
                ('FoodItems', models.CharField(max_length=255)),
                ('X', models.CharField(blank=True, max_length=255)),
                ('Y', models.CharField(blank=True, max_length=255)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Schedule', models.CharField(blank=True, max_length=255)),
                ('dayshours', models.CharField(blank=True, max_length=255)),
                ('NOISent', models.CharField(blank=True, max_length=255)),
                ('Approved', models.CharField(blank=True, max_length=255)),
                ('Received', models.CharField(blank=True, max_length=255)),
                ('PriorPermit', models.CharField(blank=True, max_length=255)),
                ('ExpirationDate', models.CharField(max_length=255)),
                ('Location', models.CharField(max_length=255)),
                ('Fire_Prevention_Districts', models.CharField(blank=True, max_length=255)),
                ('Police_Districts', models.CharField(blank=True, max_length=255)),
                ('Supervisor_Districts', models.CharField(blank=True, max_length=255)),
                ('Zip_Codes', models.CharField(blank=True, max_length=255)),
                ('Neighborhoods_old', models.CharField(blank=True, max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
