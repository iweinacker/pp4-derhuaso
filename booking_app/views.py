from django.shortcuts import render
from django.views import generic, View
from .models import Booking
from django.contrib.auth.models import User


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'base.html', {'bookings': bookings})
