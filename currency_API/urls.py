from django.contrib import admin
from django.urls import path, include
from currency_API.settings import DEBUG
from currency_API.swagger import swagger_pattern


if DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('parser.urls')),
        swagger_pattern,
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('parser.urls')),
    ]
    