from django.contrib import admin
from .models import Price
from django.utils.translation import gettext_lazy as _

class PriceAdmin(admin.ModelAdmin):

    list_display = (
        'currency', 
        'city', 
        'place',
        'prices',
        'parser_status', 
        'last_update'
    )
    list_filter = (
        'city', 
        'place',
        'currency',
        'parser_status'
    )
    fieldsets = (
        (_('Main info'), {'fields': ('currency', 'city', 'place','parser_status', 'last_update')}),
        (_('Price info'), {'fields': ('price_bid', 'price_ask')})
    )

admin.site.register(Price, PriceAdmin)

