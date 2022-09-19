from django.urls import path
from api.v1.views import CurrencyListViewSet, CurrencyViewSet

urlpatterns = [
    path("", CurrencyListViewSet.as_view(), name="currencies"),
    path("<int:pk>", CurrencyViewSet.as_view(), name="currency")
]
