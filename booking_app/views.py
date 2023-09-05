from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Customer, Table, Booking


class BookingCreate(Booking):
    model = Booking
    template_name = 'index.html'
    context_object_name = 'bookings'


class BookingUpdate(Booking):
    model = Booking
    template_name = 'index.html'
    fields = ['table', 'group', 'date_required', 'time']


class BookingDelete(Booking):
    model = Booking
    template_name = 'index.html'
    success_url = '/bookings/'
