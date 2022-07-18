from django.db import models

class Schedule(models.Model):
    departureTime = models.TextField(
        verbose_name='Время отправления',
    )
    arrivalTime = models.TextField(
        verbose_name='Время прибытия',
    )
    travelTime = models.TextField(
        verbose_name='Время в пути',
    )
    drivingMode = models.TextField(
        verbose_name='Режим движения',
    )
    trainRoute = models.TextField(
        verbose_name='Маршрут электрички',
    )
    priceAtCheckout = models.PositiveIntegerField(
        verbose_name='Цена при покупке в кассе',
    )
    TroikaCardPrice = models.PositiveIntegerField(
        verbose_name='Цена по карте \"Тройка\"',
    )
    delaysInfo = models.TextField(
        verbose_name='Информация о задержках',
        null=True,
        blank=True,
    )
    isTrainGone = models.BooleanField(
        verbose_name='Ушёл ли поезд',
        blank=True 
    )
    Link = models.URLField(
        verbose_name='Ссылка',
    )

    class Meta:
        verbose_name='Расписание'
        verbose_name_plural='Расписания электричек Тушинская → Стрешнево (бывш. Ленинградская) на сегодня'