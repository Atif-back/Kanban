from django.db import models
from datetime import datetime

from applications.custom_user.models import CustomUser


class Column(models.Model):
    """
    Модель колонки
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Модель задачи
    """
    description = models.TextField()
    status = models.CharField(max_length=100, null=True, blank=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE,
                               blank=True, null=True, related_name='tasks')
    created_at = models.CharField(max_length=20, editable=False)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now().strftime('%d-%m-%Y %H:%M')
        super().save(*args, **kwargs)

    def move_to_column(self, column):
        """
        Эта функия перемещает таск в заданную колонку
        она ничего не возвращает
        """
        self.column = column
        self.save()
