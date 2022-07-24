from django.contrib import admin
from .models import Currency, Place, City, Price

class PriceAdmin(admin.ModelAdmin):
    list_display = ('price_currency', 'price_bid', 'price_ask', 'price_city', 'price_place', 'price_status', 'price_last_updates')
    ordering = ['-price_last_updates']

admin.site.register(Price, PriceAdmin)
admin.site.register(Currency)
admin.site.register(Place)
admin.site.register(City)