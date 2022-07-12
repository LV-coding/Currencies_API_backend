import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
from django.utils import timezone
from .models import Price



def get_currency_prices(sleep_time):
    prices = Price.objects.all()

    # check if value for parsing is exist
    if prices:
        for price in prices:

            ua = UserAgent()
            headers = {
                'User-Agent':ua.random
            }
            url = f'https://minfin.com.ua/ua/currency/auction/{price.price_place}/{price.price_currency}/buy/{price.price_city}/'

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                result = []
                for i in soup.find_all('span', class_='Typography cardHeadlineL align'):
                    index = i.text.find(',') + 3
                    result.append(i.text[:index].replace(',','.'))

                price.price_bid = float(result[0])
                price.price_ask = float(result[1])
                price.price_last_updates = timezone.now()
                price.save()

                sleep(sleep_time)
            else:
                sleep(1800)
    else:
        sleep(60)