from django.urls import path
from .views import index, news

# здесь прописываем все маршруты текущего приложения
urlpatterns = [
    path('', index, name='home'),
    path('news/', news, name='news')
]