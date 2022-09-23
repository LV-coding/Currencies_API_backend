from api.v1.serializer import CurrencySerializer, CitySerializer, PriceSerializer, PlaceSerializer
from parser.models import Currency, City, Price, Place

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend


class CurrencyListViewSet(ListCreateAPIView):
    """View for create and list views Currency API endpoint."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CurrencyViewSet(RetrieveUpdateDestroyAPIView):
    """View for create, update, delete and view single Currency API endpoint."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CityListViewSet(ListCreateAPIView):
    """View for create and list views City API endpoint.""" 
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CityViewSet(RetrieveUpdateDestroyAPIView):
    """View for create, update, delete and view single City API endpoint."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlaceListViewSet(ListCreateAPIView):
    """View for create and list views Place API endpoint.""" 
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlaceViewSet(RetrieveUpdateDestroyAPIView):
    """View for create, update, delete and view single Place API endpoint."""
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
