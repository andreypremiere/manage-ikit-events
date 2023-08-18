from django.urls import path
from .views import index

# здесь прописываем все маршруты текущего приложения
urlpatterns = [
    path('', index)
]