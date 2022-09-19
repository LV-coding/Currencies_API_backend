from api.v1.serializer import CurrencySerializer, CitySerializer, PriceSerializer
from parser.models import Currency, City, Price

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

class CurrencyListViewSet(ListCreateAPIView):
    """View for create and list views Currency API endpoint."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]


class CurrencyViewSet(RetrieveUpdateDestroyAPIView):
    """View for create, update, delete and view single Currency API endpoint."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]


class CityListViewSet(ListCreateAPIView):
    """View for create and list views City API endpoint.""" 
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]


class CityViewSet(RetrieveUpdateDestroyAPIView):
    """View for create, update, delete and view single City API endpoint."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]


class PriceListViewSet(ListCreateAPIView):
    """View for create and list views Price API endpoint."""
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('currency', 'city', 'parser_status')


class PriceViewSet(RetrieveUpdateDestroyAPIView):
    """View for create, update, delete and view single Price API endpoint."""
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
