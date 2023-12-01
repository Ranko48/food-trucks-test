import csv
import os
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from foodtrucks.models import FoodTruck

class Command(BaseCommand):
    help = 'Import food truck data from CSV'

    def handle(self, *args, **options):
        # Get the path to the CSV file
        csv_file_path = self.get_csv_file_path()

        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                latitude = float(row['Latitude'])
                longitude = float(row['Longitude'])

                # Skip the iteration if both latitude and longitude are 0
                if latitude == 0 and longitude == 0:
                    continue

                location_id = row['locationid']
                # Check if a FoodTruck object with the same locationid already exists
                food_truck = FoodTruck.objects.filter(locationid=location_id).first()

                if food_truck:
                    # FoodTruck already exists, update the existing object with new values
                    food_truck.Applicant = row['Applicant']
                    food_truck.FacilityType = row['FacilityType']
                    # ... update other fields as needed ...
                    food_truck.save()
                else:
                    # FoodTruck doesn't exist, create a new object
                    food_truck = self.create_food_truck(row)
                    if food_truck:
                        food_truck.save()

    def get_csv_file_path(self):
        # Get the absolute path to the CSV file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_rel_path = '../../../food-truck-data.csv'
        csv_file_path = os.path.join(base_dir, csv_file_rel_path)
        return os.path.abspath(csv_file_path)

    def create_food_truck(self, row):
        latitude = float(row['Latitude'])
        longitude = float(row['Longitude'])

        # Skip creating the FoodTruck object if both latitude and longitude are 0
        if latitude == 0 and longitude == 0:
            return None

        # Create a Point object for the location using longitude and latitude
        location = self.create_point(longitude, latitude)

        # Create and return a new FoodTruck object
        return FoodTruck.objects.create(
            locationid=row['locationid'],
            Applicant=row['Applicant'],
            FacilityType=row['FacilityType'],
            cnn=row['cnn'],
            LocationDescription=row['LocationDescription'],
            Address=row['Address'],
            blocklot=row['blocklot'],
            block=row['block'],
            lot=row['lot'],
            permit=row['permit'],
            Status=row['Status'],
            FoodItems=row['FoodItems'],
            X=row['X'],
            Y=row['Y'],
            Latitude=row['Latitude'],
            Longitude=row['Longitude'],
            Schedule=row['Schedule'],
            dayshours=row['dayshours'],
            NOISent=row['NOISent'],
            Approved=row['Approved'],
            Received=row['Received'],
            PriorPermit=row['PriorPermit'],
            ExpirationDate=row['ExpirationDate'],
            Location=row['Location'],
            Fire_Prevention_Districts=row['Fire Prevention Districts'],
            Police_Districts=row['Police Districts'],
            Supervisor_Districts=row['Supervisor Districts'],
            Zip_Codes=row['Zip Codes'],
            Neighborhoods_old=row['Neighborhoods (old)'],
            location=location
        )

    def create_point(self, longitude, latitude):
        # Create a Point object with the given longitude and latitude
        return Point(longitude, latitude, srid=4326)