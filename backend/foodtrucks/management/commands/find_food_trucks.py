from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from foodtrucks.models import FoodTruck
import json

class Command(BaseCommand):
    help = 'Find nearby food trucks based on latitude and longitude'

    from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from foodtrucks.models import FoodTruck
import json

class Command(BaseCommand):
    help = 'Find nearby food trucks based on latitude and longitude'

    def add_arguments(self, parser):
        parser.add_argument('latitude', type=float)
        parser.add_argument('longitude', type=float)

    def handle(self, *args, **options):
        latitude = options['latitude']
        longitude = options['longitude']
        user_location = Point(longitude, latitude, srid=4326)

        # Retrieve food trucks within a certain distance (e.g., 1 kilometers)
        nearby_food_trucks = FoodTruck.objects.annotate(
                distance=Distance('location', user_location)
            ).filter(distance__lte=500).order_by('distance')

        if nearby_food_trucks.count() < 5:
            # If there are fewer than 5 trucks within 0.5 kilometers,
            # retrieve additional trucks regardless of distance
            additional_trucks = FoodTruck.objects.exclude(locationid__in=nearby_food_trucks.values_list('locationid', flat=True))[:5]

            # Concatenate the additional trucks with the nearby trucks
            nearby_food_trucks = nearby_food_trucks | additional_trucks[:5]
    
        # Serialize the food truck data into JSON format
        serialized_data = [
            {
                'applicant': truck.Applicant,
                'facilityType': truck.FacilityType,
                'address': truck.Address,
            }
            for truck in nearby_food_trucks
        ]
        # Print the serialized data as a JSON string
        json_data = json.dumps(serialized_data,  indent=5)
        print(json_data)
