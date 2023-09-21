from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date',
                    'time', 'number_of_guests')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
