from api.v1.serializer import PriceSerializer
from parser.models import Price

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend


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
