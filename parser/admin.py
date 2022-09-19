from django.contrib import admin
from .models import Currency, City, Price
from django.utils.translation import gettext_lazy as _

class PriceAdmin(admin.ModelAdmin):

    list_display = (
        'currency', 
        'city', 
        'parser_status', 
        'last_update', 
        'banks_prices', 
        'exchanger_prices', 
        'nbu_price'
    )
    list_filter = (
        'currency', 
        'city', 
        'parser_status'
    )
    fieldsets = (
        (_('Main info'), {'fields': ('currency', 'city', 'parser_status', 'last_update')}),
        (_('Price info'), {'fields': ('bank_price_bid', 'bank_price_ask', 'exchanger_price_bid', 'exchanger_price_ask', 'nbu_price')})
    )

admin.site.register(Price, PriceAdmin)
admin.site.register(Currency)
admin.site.register(City)
