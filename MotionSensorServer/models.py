from django.db import models


class Sensor(models.Model):
	name = models.TextField()
	activated = models.BooleanField()


class SensorReading(models.Model):
	sensor = models.ForeignKey(Sensor, null=False)
	date = models.DateTimeField()
	detected = models.BooleanField(default=False)
