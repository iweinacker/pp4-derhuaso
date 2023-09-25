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


class ReservationForm(forms.ModelForm):
    class Meta:
        model: Booking
        fields = ('first_name', 'last_name', 'phone',
                  'minimum_people', 'maximum_people', 'date_required'
                  'time'
                  )

        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'minimun_people': forms.TextInput(attrs={'class': 'form-control'}),
            'maximum_people': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
        }

    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    # phone = forms.CharField(max_length=100)
    # seats = forms.IntegerField()
    # minimum_people = forms.IntegerField()
    # maximum_people = forms.IntegerField()
    # date_required = forms.DateField()
    # time = forms.ChoiceField(choices=HOURS, initial="6 PM")
