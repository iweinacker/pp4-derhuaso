from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Booking
from django.utils import timezone

HOURS = (
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8 PM", "8 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9 PM", "9 PM"),
    ("9:30 PM", "9:30 PM"),
    ("10 PM", "10 PM"),
)

SEATS = (
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
)


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

    # def clean_date_required(self):
    #     date_required = self.cleaned_data['date_required']
    #     if date_required and date_required < timezone.localdate():
    #         raise ValidationError("Date cannot be in the past")
    #     return date
