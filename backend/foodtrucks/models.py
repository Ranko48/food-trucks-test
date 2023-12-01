from django.db import models
from django.contrib.gis.db.models import PointField

class FoodTruck(models.Model):
    locationid = models.IntegerField(primary_key=True)
    Applicant = models.CharField(max_length=255)
    FacilityType = models.CharField(max_length=255)
    cnn = models.IntegerField()
    LocationDescription = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    blocklot = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    permit = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    FoodItems = models.CharField(max_length=255)
    X = models.CharField(max_length=255, blank=True)
    Y = models.CharField(max_length=255, blank=True)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Schedule = models.CharField(max_length=255, blank=True)
    dayshours = models.CharField(max_length=255, blank=True)
    NOISent = models.CharField(max_length=255, blank=True)
    Approved = models.CharField(max_length=255, blank=True)
    Received = models.CharField(max_length=255, blank=True)
    PriorPermit = models.CharField(max_length=255, blank=True)
    ExpirationDate = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Fire_Prevention_Districts = models.CharField(max_length=255, blank=True)
    Police_Districts = models.CharField(max_length=255, blank=True)
    Supervisor_Districts = models.CharField(max_length=255, blank=True)
    Zip_Codes = models.CharField(max_length=255, blank=True)
    Neighborhoods_old = models.CharField(max_length=255, blank=True)
    location = PointField()

    def __str__(self):
        return self.Applicant