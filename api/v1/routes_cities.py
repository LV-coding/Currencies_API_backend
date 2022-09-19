from django.urls import path
from api.v1.views import CityListViewSet, CityViewSet

urlpatterns = [
    path("", CityListViewSet.as_view(), name="cities"),
    path("<int:pk>", CityViewSet.as_view(), name="city")
]
