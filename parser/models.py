from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    name = models.CharField(_('Currency name'), max_length=3)
    title = models.CharField(_('Currency title'), max_length=64)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(_('City name'), max_length=128) # english name in Minfin
    title = models.CharField(_('City title'), max_length=128) # user name

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(_('Place name'), max_length=128) # english name in Minfin
    title = models.CharField(_('Place title'), max_length=128) # user name

    def __str__(self):
        return self.name


class Price(models.Model):
    currency = models.ForeignKey(
        Currency, 
        on_delete=models.CASCADE, 
        related_name='currency', 
        verbose_name=_('Currency')
    )
    city = models.ForeignKey(
        City, 
        on_delete=models.CASCADE, 
        related_name='city', 
        verbose_name=_('City')
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='place',
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
