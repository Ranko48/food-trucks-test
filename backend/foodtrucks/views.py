from django.http import JsonResponse
from django.views import View
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import FoodTruck

class NearbyFoodTrucksView(View):
    def get(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        if latitude and longitude:
            user_location = Point(float(longitude), float(latitude), srid=4326)

            # Retrieve food trucks within a certain distance (e.g., 0.5 kilometers)
            nearby_food_trucks = FoodTruck.objects.annotate(
                distance=Distance('location', user_location)
            ).filter(distance__lte=500, distance__gt=0).order_by('distance')

            if nearby_food_trucks.count() < 5:
                # If there are fewer than 5 trucks within 0.5 kilometers,
                # retrieve additional trucks regardless of distance
                additional_trucks = FoodTruck.objects.exclude(locationid__in=nearby_food_trucks.values_list('locationid', flat=True))[:5]

                # Concatenate the additional trucks with the nearby trucks
                nearby_food_trucks = nearby_food_trucks | additional_trucks[:5]
            data = {
                'food_trucks':[
                    {
                        'id': truck.locationid,
                        'name': truck.Applicant,
                        'facility_type': truck.FacilityType,
                        'address': truck.Address,
                        'lat': truck.Latitude,
                        'lng': truck.Longitude,
                        'distance': truck.distance.m
                    }
                    for truck in nearby_food_trucks
                ]
            }
            # Return result as Json
            return JsonResponse(data)
        else:
            # Will return error when Latitude and Longitude prameters are invalid
            return JsonResponse({'error': 'Latitude and longitude parameters are required.'}, status=400)
