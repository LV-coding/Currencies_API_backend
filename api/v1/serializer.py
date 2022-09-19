from parser.models import Price, Currency, City
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model= Currency
        fields = ('name', 'title')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields = ('name', 'title')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Price
        fields = (
            'currency', 
            'city', 
            'bank_price_ask', 
            'bank_price_bid', 
            'exchanger_price_ask', 
            'exchanger_price_bid', 
            'nbu_price', 
            'parser_status', 
            'last_update'
        )
        