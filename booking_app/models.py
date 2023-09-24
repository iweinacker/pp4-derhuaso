from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from cloudinary.models import CloudinaryField

HOURS = (
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8 PM", "8 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9 PM", "9 PM"),
    ("9:30 PM", "9:30 PM"),
    ("10 PM", "10 PM"),
)

class Customer(models.Model):
    first_name = models.CharField(max_length=50, unique=True, blank=True,
                                  editable=True)
    last_name = models.CharField(max_length=50, unique=True, blank=True,
                                 editable=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True, blank=True,
                                 editable=True)

class Table(models.Model):
    seats = models.IntegerField()
    minimun_people = models.IntegerField()
    maximum_people = models.IntegerField()


class Booking(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    group = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date_required = models.DateField()
    time = models.CharField(max_length=20, choices=HOURS, default="6:00 PM")
    day = models.DateTimeField(default=timezone.now, blank=True)
    date_updated = models.DateTimeField(default=timezone.now, blank=True)



