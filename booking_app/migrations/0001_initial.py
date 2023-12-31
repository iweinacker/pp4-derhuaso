# Generated by Django 3.2.21 on 2023-09-05 10:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=50, unique=True)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('minimun_people', models.IntegerField()),
                ('maximum_people', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_required', models.DateField()),
                ('date_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.customer')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.table')),
            ],
        ),
    ]
