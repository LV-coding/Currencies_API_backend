from django.urls import path
from parser.views import force_update, activate_second_thread, show_active_thread

urlpatterns = [
    path('force_update/', force_update, name='force_update'),
    path('activate_second_thread/', activate_second_thread, name='activate_second_thread'),
    path('active_thread/', show_active_thread, name='active_thread'),
]
