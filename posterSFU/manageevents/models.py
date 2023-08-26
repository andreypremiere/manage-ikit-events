from django.db import models
from django.urls import reverse


class ListUniversity(models.Model):
    """
    Класс для формирования списка институтов.
    """
    # id формируется автоматически
    title = models.CharField(max_length=20)


    def __str__(self):
        return self.title


class Events(models.Model):
    """
    Класс для формирования мероприятий
    """
    title = models.CharField(max_length=50, verbose_name='Название')
    date_of_event = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Дата мероприятия')
    time_of_event = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время мероприятия')
    description = models.TextField(max_length=255, verbose_name='Описание')
    preview = models.ImageField(upload_to="preview/%Y/%m/", verbose_name='Превью')
    need_team = models.BooleanField(verbose_name='Необходимость команды',)
    quantity_of_participant = models.IntegerField(verbose_name='Количество участников',)
    all_free_place = models.IntegerField(verbose_name='Свободные места',)
    place_of_meeting = models.CharField(max_length=100, verbose_name='Место встречи')
    organizer = models.ForeignKey('ListUniversity', on_delete=models.PROTECT, verbose_name='Организатор')


    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('events', kwargs={'event_id': self.pk})

    # Специальный класс для отображения в админ-панели
    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'
        ordering = ['date_of_event', 'time_of_event']
