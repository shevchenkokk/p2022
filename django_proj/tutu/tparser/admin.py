from django.contrib import admin

from .models import Schedule
from .forms import ScheduleForm

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('departureTime', 
    'arrivalTime', 
    'travelTime', 
    'drivingMode', 
    'trainRoute', 
    'priceAtCheckout', 
    'TroikaCardPrice',
    'delaysInfo',
    'isTrainGone',
    'Link')
    list_filter = ('isTrainGone', )

    form = ScheduleForm
