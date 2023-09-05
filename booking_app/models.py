from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Customer(models.Model):
    first_name = models.CharField(max_length=50, unique=True, blank=True,
                                  editable=True)
    last_name = models.CharField(max_length=50, unique=True, blank=True,
                                 editable=True)
    phone = models.CharField(max_length=100)


class Table(models.Model):
    seats = models.IntegerField()
    minimun_people = models.IntegerField()
    maximum_people = models.IntegerField()


class Booking(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    group = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date_required = models.DateField()
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_updated = models.DateTimeField(default=timezone.now, blank=True)

