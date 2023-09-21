from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} | day: {self.date} | time: {self.time}"
