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

SEATS = (
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
)


class Booking(models.Model):
    first_name = models.CharField(max_length=50, unique=True,
                                  blank=True, editable=True)
    last_name = models.CharField(max_length=50, unique=True,
                                 blank=True, editable=True)
    phone = models.CharField(max_length=100, default='1234567890')
    email = models.CharField(max_length=50, unique=True,
                             blank=True, editable=True)
    seats = models.IntegerField(default=2, choices=SEATS)
    date_required = models.DateTimeField(default=timezone.now, blank=True)
    time = models.CharField(max_length=20, choices=HOURS, default="6:00 PM")
    day = models.DateTimeField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):

        super(Booking, self).save(*args, **kwargs)
