from django.contrib import admin
from .models import Customer, Table, Booking


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    search_fields = ('first_name', 'last_name', 'phone')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('seats', 'minimun_people', 'maximum_people')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('table', 'group', 'date_required',
                    'date_created', 'date_updated')
    list_filter = ('table', 'group', 'date_required')
