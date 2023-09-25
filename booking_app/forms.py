from django import forms
from django.forms import ModelForm
from .models import Booking

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
        fields = ('first_name', 'last_name', 'phone',
                  'seats', 'date_required', 'time')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'seats': forms.Select(attrs={'class': 'form-control'}),
            'date_required': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
        }
