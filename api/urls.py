from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('force_update/', views.force_update, name='force_update'),
    path('api/', views.general_serialization, name='general_serialization'),
    path('api/<currency>', views.currency_serialization, name='currency_serialization'),
    path('api/<currency>/<city>/<place>', views.detailed_serialization, name='detailed_serialization'),
    path('activate_second_thread/', views.activate_second_thread, name='activate_second_thread')
]
