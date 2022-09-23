from django.contrib import admin
from .models import Currency, City, Price, Place
from django.utils.translation import gettext_lazy as _

class PriceAdmin(admin.ModelAdmin):

    list_display = (
        'currency', 
        'city', 
        'place',
        'parser_status', 
        'last_update', 
        'prices'
    )
    list_filter = (
        'currency', 
        'city', 
        'place',
        'parser_status'
    )
    fieldsets = (
        (_('Main info'), {'fields': ('currency', 'city', 'place','parser_status', 'last_update')}),
        (_('Price info'), {'fields': ('price_bid', 'price_ask')})
    )

admin.site.register(Price, PriceAdmin)
admin.site.register(Currency)
admin.site.register(City)
admin.site.register(Place)
