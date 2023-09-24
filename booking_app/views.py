from django.shortcuts import render,  redirect
from .models import Booking, Table, Customer
from django.contrib.auth.models import User
from .forms import ReservationForm


def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            customer = Customer(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone']
            )
            customer.save()

            table = Table(
                seats=form.cleaned_data['seats'],
                minimum_people=form.cleaned_data['minimum_people'],
                maximum_people=form.cleaned_data['maximum_people']
            )
            table.save()

            booking = Booking(
                table=table,
                group=customer,
                date_required=form.cleaned_data['date_required'],
                time=form.cleaned_data['time']
            )
            booking.save()

            return redirect('success')
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})
