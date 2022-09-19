import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
from django.utils import timezone


def get_currency_prices(sleep_time):
    # if migrations is not exist
    try:
        from parser.models import Price
        prices = Price.objects.filter(parser_status=True)
    except:
        prices = []

    # check if value for parsing is exist
    if prices:
        for price in prices:

            ua = UserAgent()
            headers = {
                'User-Agent':ua.random
            }
            url = f'https://minfin.com.ua/ua/currency/{price.city}/{price.currency}/'

            try:
                response = requests.get(url, headers=headers, timeout=4)
            except:
                sleep(300)
                continue

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                result = []
                for i in soup.find_all('span', class_='mfm-posr'):
                    index = i.text.find('.') + 3
                    result.append(i.text[:index])

                price.bank_price_bid = float(result[0])
                price.bank_price_ask = float(result[1])
                price.exchanger_price_bid = float(result[2])
                price.exchanger_price_ask = float(result[3])
                price.nbu_price = float(result[4])
                price.last_update = timezone.now()
                price.save()

                sleep(sleep_time)
            else:
                sleep(300)
    else:
        sleep(60)
