from django.http import HttpResponse
from django.shortcuts import render


# Обязательный параметр request.
# Функцию представления нужно связывать с соответствующим url-адресом.
def index(request):
    return HttpResponse('Страница приложения')



