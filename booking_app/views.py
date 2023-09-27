from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Booking
from django.contrib.auth.models import User
from .forms import ReservationForm


def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                # Save the form data to the database
                booking = Booking(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone=form.cleaned_data['phone'],
                    seats=form.cleaned_data['seats'],
                    date_required=form.cleaned_data['date_required'],
                    time=form.cleaned_data['time'],
                )
                booking.save()

                return redirect('success')
            pass
    else:
        form = ReservationForm()

    return render(request, 'index.html', {'form': form})


# class ReservationView(ListView):
#     model = Booking
#     template_name = 'index.html'

#     def get(self, request):
#         return render(request, 'index.html', {'form': ReservationForm})

#     def post(self, request):
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             booking = Booking(
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 phone=form.cleaned_data['phone'],
#                 seats=form.cleaned_data['seats'],
#                 date_required=form.cleaned_data['date_required'],
#                 time=form.cleaned_data['time'],
#             )
#             booking.save()

#             return redirect('success')

#         return render(request, 'index.html', {'form': ReservationForm})
