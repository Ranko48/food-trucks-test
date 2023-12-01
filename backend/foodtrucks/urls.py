from django.urls import path
from foodtrucks.views import NearbyFoodTrucksView

urlpatterns = [
    path('nearby-food-trucks/', NearbyFoodTrucksView.as_view(), name='nearby-food-trucks'),
]
