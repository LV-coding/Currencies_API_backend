from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyChoice(models.TextChoices):
    USD = 'usd', _('US dollar')
    EUR = 'eur', _('Euro')
    PLN = 'pln', _('Polish zloty')
    AUD = 'aud', _('Australian dollar')
    NOK = 'nok', _('Norwegian krone')
    DKK = 'dkk', _('Danish krone')
    CAD = 'cad', _('Canadian dollar')
    CNY = 'cny', _('Chinese yuan renminbi')
    TRY = 'try', _('Turkish lira')
    JPY = 'jpy', _('Japanese yen')
    ILS = 'ils', _('Israeli shekel')
    CHF = 'chf', _('Swiss franc')
    GBP = 'gbp', _('Pound sterling')
    SEK = 'sek', _('Swedish krona')


class PlaceChoice(models.TextChoices):
    BANKS = 'banks', _('Banks')
    EXCHANGER = 'exchanger', _('Exchanger')
    MARKET = 'market', _('Market')


class CityChoice(models.TextChoices):
    LVIV = 'lvov', _('Lviv')
    KYIV = 'kiev', _('Kyiv')
