from django.contrib import admin
from .models import Customer, Booking, Table


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'phone', 'email')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('seats', 'minimun_people', 'maximum_people')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('table', 'group', 'date_required',
                    'day', 'time')
    list_filter = ('table', 'group', 'day')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
