import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
from django.utils import timezone
from parser.models import Price

def get_currency_prices(sleep_time):
 
    prices = Price.objects.filter(parser_status=True)

    if prices:
        for price in prices:

            ua = UserAgent()
            headers = {
                'User-Agent':ua.random
            }
            url = f'https://minfin.com.ua/ua/currency/auction/{price.place}/{price.currency}/buy/{price.city}/'

            try:
                response = requests.get(url, headers=headers, timeout=4)
            except:
                sleep(300)
                continue

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                result = []
                for i in soup.find_all('span', class_='Typography cardHeadlineL align'):
                    index = i.text.find(',') + 3
                    result.append(i.text[:index].replace(',','.'))
                if result[0] != '0.00' and result[1] != '0.00':
                    price.price_bid = float(result[0])
                    price.price_ask = float(result[1])
                    price.last_update = timezone.now()
                    price.save()

                sleep(sleep_time)
            else:
                sleep(300)
    else:
        sleep(60)
