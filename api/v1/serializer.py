from parser.models import Price
from rest_framework import serializers


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
        