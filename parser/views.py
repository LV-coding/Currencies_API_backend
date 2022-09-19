from django.http import HttpResponse, HttpResponseForbidden
from parser.parser import get_currency_prices
from threading import Thread, active_count

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
        thread_2.start()
        return HttpResponse('Другий потік запущено!')
    else:
        return HttpResponseForbidden('Доступ заборонений')    

# for admins
def show_active_thread(request):
    if request.user.is_superuser:
        msg = f'Активних потоків: {active_count()}.\nРобота парсера: {thread_2.is_alive()}.'
        return HttpResponse(msg)
    else:
        return HttpResponseForbidden('Доступ заборонений')  

def background_parser():
    while True:
        get_currency_prices(120)


thread_2 = Thread(target=background_parser, daemon=True)
thread_2.start()
