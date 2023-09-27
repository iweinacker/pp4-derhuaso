from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'seats',
                    'date_required', 'day', 'time')
    search_fields = ('first_name', 'last_name',
                     'email', 'day')



# @admin.register(Table)
# class TableAdmin(admin.ModelAdmin):
#     list_display = ('seats', 'minimun_people', 'maximum_people')


# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('table', 'group', 'date_required',
#                     'day', 'time')
#     list_filter = ('table', 'group', 'day')
#     actions = ['approve_bookings']
