from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking
from django.contrib.auth.models import User
from .forms import ReservationForm


class ReservationView(generic.ListView):
    model: Booking
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'index.html', {'form': ReservationForm})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            Booking = Booking(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                seats=form.cleaned_data['seats'],
                date_required=form.cleaned_data['date_required'],
                time=form.cleaned_data['time'],
            )
            Booking.save()

            # table = Table(
            #     seats=form.cleaned_data['seats'],
            #     minimum_people=form.cleaned_data['minimum_people'],
            #     maximum_people=form.cleaned_data['maximum_people']
            # )
            # table.save()

            # booking = Booking(
            #     table=table,
            #     group=customer,
            #     date_required=form.cleaned_data['date_required'],
            #     time=form.cleaned_data['time']
            # )
            # booking.save()

            return redirect('success')

        return render(request, 'index.html', {'form': ReservationForm})
