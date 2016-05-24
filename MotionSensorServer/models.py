from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.forms import ModelForm


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    custom_id = models.CharField(null=False, unique=True, max_length=10)
    activated = models.BooleanField()


class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, null=False)
    date_from = models.DateTimeField(null=False)
    date_to = models.DateTimeField(null=False)
    detected = models.BooleanField(default=False)


class UserSensor(models.Model):
    user = models.ForeignKey(User)
    sensor = models.ForeignKey(Sensor)


class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'custom_id', 'activated']
