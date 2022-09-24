from django.contrib import admin
from django.urls import path, include
from currency_API.settings import DEBUG
from currency_API.swagger import swagger_pattern


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-action/', include('parser.urls')),
    path('api/v1/currencies/', include('api.v1.routes')),
]
if DEBUG:
    urlpatterns.append(swagger_pattern)
    