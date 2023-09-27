from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Booking
from django.contrib.auth.models import User
from .forms import ReservationForm
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse


from django.contrib import messages


def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            booking = Booking(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                seats=form.cleaned_data['seats'],
                date_required=form.cleaned_data['date_required'],
                time=form.cleaned_data['time'],
            )
            booking.save()

            messages.success(
                request, 'Booking complete, we are checking our availability, please wait for a call back.'
                 )
        else:
            messages.error(
                request, 'There was an error with your submission. Please try again.'
                 )
    else:
        form = ReservationForm()

    return render(request, 'index.html', {'form': form})
