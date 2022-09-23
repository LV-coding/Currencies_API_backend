from parser.models import Price, Currency, City, Place
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model= Currency
        fields = ('name', 'title')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields = ('name', 'title')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Place
        fields = ('name', 'title')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Price
        fields = (
            'currency', 
            'city', 
            'place',
            'price_ask', 
            'price_bid', 
            'parser_status', 
            'last_update'
        )
        