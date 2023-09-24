# Generated by Django 3.2.21 on 2023-09-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date_created',
            new_name='day',
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM'), ('8 PM', '8 PM'), ('8:30 PM', '8:30 PM'), ('9 PM', '9 PM'), ('9:30 PM', '9:30 PM'), ('10 PM', '10 PM')], default='6:00 PM', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
