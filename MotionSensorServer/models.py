from django.contrib.auth.models import User
from django.db import models


class Sensor(models.Model):
    name = models.TextField()
    custom_id = models.TextField(null=False, unique=True)
    activated = models.BooleanField()


class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, null=False)
    date = models.DateTimeField()
    detected = models.BooleanField(default=False)


class UserSensors(models.Model):
    user = models.ForeignKey(User)
    sensor = models.ForeignKey(Sensor)
