from django import forms
from .models import Customer, Table, Booking


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

class ReservationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=100)
    seats = forms.IntegerField()
    minimum_people = forms.IntegerField()
    maximum_people = forms.IntegerField()
    date_required = forms.DateField()
    time = forms.ChoiceField(choices=HOURS, initial="6 PM")



