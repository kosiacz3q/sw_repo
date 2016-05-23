from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from MotionSensorServer.models import Sensor, SensorReading
import datetime
from .models import SensorForm, UserSensor


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


@login_required()
def new_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            try:
                my_new_sensor = form.save()
                UserSensor.objects.get_or_create(user=request.user, sensor=my_new_sensor)
                return HttpResponseRedirect('/')
            except:
                pass
    return render_to_response('MotionSensorServer/new_sensor.html', {'form': SensorForm()},
                              context_instance=RequestContext(request))


@login_required()
def get_sensors(request):
    user_sensors = [i.sensor for i in UserSensor.objects.filter(user__exact=request.user)]
    return render_to_response('MotionSensorServer/sensors.html', {
        "items": user_sensors
    }, RequestContext(request))


@login_required()
def get_detections(request):
    user_sensors = [i.sensor for i in UserSensor.objects.filter(user__exact=request.user)]
    detections = SensorReading.objects.order_by("date")
    detections = [i for i in detections if i.sensor in user_sensors]
    return render_to_response('MotionSensorServer/detections.html', {
        "items": detections
    }, RequestContext(request))
