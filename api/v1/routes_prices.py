from django.urls import path
from api.v1.views import PriceListViewSet, PriceViewSet

urlpatterns = [
    path("", PriceListViewSet.as_view(), name="prices"),
    path("<int:pk>", PriceViewSet.as_view(), name="price")
]
