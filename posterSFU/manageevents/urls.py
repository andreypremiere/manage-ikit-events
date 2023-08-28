from django.urls import path
from .views import index, news, show_events, show_institutes

# здесь прописываем все маршруты текущего приложения
urlpatterns = [
    path('', index, name='home'),
    path('news/', news, name='news'),
    path('events/<int:event_id>', show_events, name='events'),
    path('institutes/<int:institute_id>', show_institutes, name='institutes')
]