from django import forms

from .models import Schedule

class ScheduleForm(forms.ModelForm):
    
    class Meta:
        model = Schedule
        fields = (
            'departureTime', 
            'arrivalTime', 
            'travelTime', 
            'drivingMode', 
            'trainRoute', 
            'priceAtCheckout', 
            'TroikaCardPrice',
            'delaysInfo',
            'isTrainGone',
            'Link')
        widgets = {
            'departureTime': forms.TextInput,
            'arrivalTime': forms.TextInput,
            'travelTime': forms.TextInput,
            'drivingMode': forms.TextInput,
            'trainRoute': forms.TextInput,
            'delaysInfo': forms.TextInput,
        }