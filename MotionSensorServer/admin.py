from django.contrib import admin
from .models import Sensor, UserSensor

admin.site.register(Sensor)
admin.site.register(UserSensor)