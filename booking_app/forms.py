from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Booking
from django.utils import timezone


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'phone', 'email',
                  'seats', 'date_required', 'time')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'seats': forms.Select(attrs={'class': 'form-control'}),
            'date_required': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
        }

