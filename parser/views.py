from django.http import HttpResponse, HttpResponseForbidden
from parser.parser import get_currency_prices
from threading import Thread, active_count


def force_update(request):
    if request.user.is_authenticated:
        get_currency_prices(0)
        return HttpResponse('Примусово оновлено всі дані!')
    return HttpResponseForbidden('ACCESS DENIED')


def activate_second_thread(request):
    if request.user.is_authenticated:
        thread_2.start()
        return HttpResponse('Другий потік запущено!')
    return HttpResponseForbidden('ACCESS DENIED')


def show_active_thread(request):
    if request.user.is_authenticated:
        msg = f'Активних потоків: {active_count()}.\nРобота парсера: {thread_2.is_alive()}.'
        return HttpResponse(msg)
    return HttpResponseForbidden('ACCESS DENIED')


def background_parser():
    while True:
        get_currency_prices(120)


thread_2 = Thread(target=background_parser, daemon=True)
#thread_2.start()
