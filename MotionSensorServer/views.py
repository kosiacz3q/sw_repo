from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from MotionSensorServer.models import Sensor, SensorReading
import datetime


def index(request):
    return render_to_response("MotionSensorServer/index.html", {
                'user': request.user,
    }, RequestContext(request))


@require_http_methods(["POST"])
def reading(request, custom_id, is_motion_detected):
    if Sensor.objects.get(custom_id=custom_id).exist():
        sensor = Sensor.objects.get(custom_id=custom_id)
        if sensor.activated:
            sensor_reading = SensorReading(
                sensor=sensor,
                date=datetime.datetime.now().time(),
                detected=(is_motion_detected == 1))

            sensor_reading.save()
    pass
