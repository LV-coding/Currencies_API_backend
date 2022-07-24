from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from .parser import get_currency_prices
from .models import Price, Currency, City, Place
from django.utils import timezone
from threading import Thread, active_count
from django.utils.timezone import localtime 
from django.views.decorators.http import require_GET


def index(request):
    currencies = Currency.objects.all()
    if request.method == 'POST':
        search = request.POST.get('currency')
        curr = Currency.objects.get(currency_name=search)
        result = Price.objects.filter(price_currency=curr)

        return render(request, 'api/index.html', {
        'currencies' : currencies,
        'result_of_search': result,
        'curr' : curr
        })
    else:
        return render(request, 'api/index.html', {
            'currencies' : currencies
        })


# for admins
def force_update(request):
    if request.user.is_superuser:
        get_currency_prices(0)
        return HttpResponse('Примусово оновлено всі дані!')
    else:
        return HttpResponseForbidden('Доступ заборонений')

# for admins
def activate_second_thread(request):
    if request.user.is_superuser:
        thread_5.start()
        return HttpResponse('Другий потік запущено!')
    else:
        return HttpResponseForbidden('Доступ заборонений')    

# for admins
def show_active_thread(request):
    if request.user.is_superuser:
        msg = f'Активних потоків: {active_count()}.\nРобота парсера: {thread_5.is_alive()}.'
        return HttpResponse(msg)
    else:
        return HttpResponseForbidden('Доступ заборонений')  

@require_GET
def general_serialization(request):
    prices = Price.objects.filter(price_status=True)
    prices = [ price.serialize() for price in prices]
    now = localtime(timezone.now())
    response = {
        'request_time' : str(now),
        'data' : prices
    }
    return JsonResponse(response)

@require_GET
def currency_serialization(request, currency):
    now = localtime(timezone.now())
    try:
        request_currency = Currency.objects.get(currency_name=currency)
    except Currency.DoesNotExist:
        return JsonResponse({'data' : 'requested currency is missing...'})

    prices = Price.objects.filter(price_status=True, price_currency=request_currency)
    
    if prices: 
        prices = [ price.serialize() for price in prices ]
    else:
        prices = 'there are no active currency positions...'

    response = {
        'request_time' : str(now),
        'data' : prices
    }
    return JsonResponse(response)

@require_GET
def detailed_serialization(request, currency, city, place):
    now = localtime(timezone.now())
    try:
        request_currency = Currency.objects.get(currency_name=currency)
        request_city = City.objects.get(city_name=city)
        request_place = Place.objects.get(place_name=place)
    except Currency.DoesNotExist:
        return JsonResponse({'data': 'requested currency is missing...'})
    except City.DoesNotExist: 
        return JsonResponse({'data': 'requested city is missing...'})
    except Place.DoesNotExist: 
        return JsonResponse({'data': 'requested place is missing...'})

    try:
        price = Price.objects.get(price_status=True, 
                                    price_currency=request_currency,
                                    price_city=request_city,
                                    price_place=request_place )

    except Currency.DoesNotExist:
        response = {
            'request_time' : str(now),
            'data' : 'requested data is missing...'
            }
        return JsonResponse(response)

    else:
        response = {
            'request_time' : str(now),
            'data' : price.serialize()
            }
        return JsonResponse(response)
        


def background_parser():
    while True:
        get_currency_prices(120)


thread_5 = Thread(target=background_parser, daemon=True)
thread_5.start()