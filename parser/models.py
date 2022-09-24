from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from parser.mchoices import CurrencyChoice, PlaceChoice, CityChoice


class Price(models.Model):
    currency = models.CharField(
        choices=CurrencyChoice.choices, 
        max_length=64,
        verbose_name=_('Currency')
    )
    city = models.CharField(
        choices=CityChoice.choices, 
        max_length=64,
        verbose_name=_('City')
    )
    place = models.CharField(
        choices=PlaceChoice.choices, 
        max_length=64,
        verbose_name=_('Place')
    )
    price_ask = models.DecimalField(
        decimal_places=2, 
        max_digits=10, 
        blank=True,
        null=True,
        verbose_name=_('Price ask'), 
    )
    price_bid = models.DecimalField(
        decimal_places=2, 
        max_digits=10, 
        blank=True, 
        null=True,
        verbose_name=_('Price bid'), 
    )
    parser_status = models.BooleanField(
        default=True, 
        verbose_name=_('Parser status')
    )
    last_update = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Last update')
    )

    class Meta:
        ordering = ('-last_update',)

    def __str__(self):
        return f'{self.currency}, {self.city}'

    @property
    def prices(self):
        return f'{self.price_bid}/{self.price_ask}'
