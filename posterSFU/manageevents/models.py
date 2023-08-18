from django.db import models


class ListUniversity(models.Model):
    """
    Класс для формирования списка институтов.
    """
    # id формируется автоматически
    title = models.CharField(max_length=20)
