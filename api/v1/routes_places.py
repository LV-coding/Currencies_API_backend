from django.urls import path
from api.v1.views import PlaceListViewSet, PlaceViewSet

urlpatterns = [
    path("", PlaceListViewSet.as_view(), name="places"),
    path("<int:pk>", PlaceViewSet.as_view(), name="place")
]
