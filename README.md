# Currency price in Ukraine
This project parses currency price data in Ukraine and distributes them via API (json format).

[![Django](https://img.shields.io/badge/Django-4.0.6-green?style=for-the-badge)](https://docs.djangoproject.com/en/4.0/)
[![Django REST framework](https://img.shields.io/badge/DRF-3.13.1-green?style=for-the-badge)](https://www.django-rest-framework.org/)
[![PostreSQL](https://img.shields.io/badge/PostreSQL-14.5-green?style=for-the-badge)](https://www.postgresql.org/docs/)
[![Beautiful Soup](https://img.shields.io/badge/BeautifulSoup-4.11.1-green?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Site is available at [LINK old version](https://currency-in-ukraine.herokuapp.com).
```bash
# To check the available list of currencies
GET: currency-in-ukraine.herokuapp.com/api/v1/currencies/
GET: currency-in-ukraine.herokuapp.com/api/v1/currencies/<id>

# To check the available list of cities
GET: currency-in-ukraine.herokuapp.com/api/v1/cities/
GET: currency-in-ukraine.herokuapp.com/api/v1/cities/<id>

# To access currency prices
GET: currency-in-ukraine.herokuapp.com/api/v1/prices/
GET: currency-in-ukraine.herokuapp.com/api/v1/prices/<id>
```
