from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.username


class Employee(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Номер телефона', max_length=255, unique=True)

    def __str__(self):
        return self.name


class TradePoint(models.Model):
    name = models.CharField('Название', max_length=255)
    employee = models.ForeignKey(Employee, verbose_name='Работник', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    date = models.DateTimeField('Дата/время', auto_now_add=True)
    trade_point = models.ForeignKey(TradePoint, verbose_name='Торговая точка', on_delete=models.CASCADE)
    latitude = models.FloatField('Широта', default=None)
    longitude = models.FloatField('Долгота', default=None)
