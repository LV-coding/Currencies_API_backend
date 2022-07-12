from django.utils import timezone
from django.db import models
from django.utils.timezone import localtime 

class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency_name = models.CharField(max_length=3)

    def __str__(self):
        return self.currency_name


class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=32)

    def __str__(self):
        return self.place_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=64) # english name in site
    city_title = models.CharField(max_length=64) # user name

    def __str__(self):
        return self.city_name


class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    price_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency')
    price_place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place')
    price_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    price_ask = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    price_bid = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    price_status = models.BooleanField(default=False)
    price_last_updates = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.price_currency}: {self.price_bid}/{self.price_ask}'

    def serialize(self):
        return {
            'id' : str(self.price_id),
            'currency': str(self.price_currency),
            'city' : str(self.price_city),
            'place' : str(self.price_place),
            'ask' : str(self.price_ask),
            'bid' : str(self.price_bid),
            'last_update' : str(localtime(self.price_last_updates))
        }

