from django.contrib import admin
from .models import Sensor, UserSensor, SensorReading

admin.site.register(Sensor)
admin.site.register(UserSensor)
admin.site.register(SensorReading)
