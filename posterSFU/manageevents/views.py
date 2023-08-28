from django.http import HttpResponse
from django.shortcuts import render
from .models import ListUniversity, Events


# Обязательный параметр request.
# Функцию представления нужно связывать с соответствующим url-адресом.
def index(request):
    # В эту переменную сохраняем записи из базы данных модели ListUniversity (вернет список?)
    list_university = ListUniversity.objects.all()
    posts = Events.objects.all()
    # Параметры и переменные, которые передаются на html страницу, передаются третьим аргументом в виде словаря
    return render(request, 'manageevents/index.html', {'title': 'Главная страница',
                                                       'list_university': list_university, 
                                                       'posts': posts,
                                                       'cat_selected': 0})


def news(request):
    return render(request, 'manageevents/news.html', {'title': 'Новости'})

def show_events(request, event_id):
    return HttpResponse(f'id {event_id}')

def show_institutes(request, institute_id):
    list_university = ListUniversity.objects.all()
    posts = Events.objects.filter(organizer_id=institute_id)
    if len(posts) == 0:
        return HttpResponse('В данном институте нет мероприятий в ближайшее время(((')
    return render(request, 'manageevents/index.html', {'title': 'Главная страница',
                                                       'list_university': list_university, 
                                                       'posts': posts,
                                                       'cat_selected': institute_id})