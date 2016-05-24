from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from MotionSensorServer.models import Sensor, SensorReading, SensorForm, UserSensor
from django.utils import timezone
from django.core.urlresolvers import reverse


def index(request):
    return render_to_response("MotionSensorServer/index.html", {
        'user': request.user,
    }, RequestContext(request))


@require_http_methods(["POST"])
@csrf_exempt
def reading(request, custom_id, is_motion_detected):

    motion_detected = (is_motion_detected == '1')

    if Sensor.objects.filter(custom_id=custom_id).exists():

        create_new = False

        sensor = Sensor.objects.get(custom_id=custom_id)
        if sensor.activated:

            if SensorReading.objects.filter(sensor=sensor).exists():
                last_reading = SensorReading.objects.filter(sensor=sensor).latest('date_from')

                last_reading.date_to = timezone.now()
                last_reading.save()

                create_new = (last_reading.detected != motion_detected)
            else:
                create_new = True

            if create_new:
                sensor_reading = SensorReading(
                    sensor=sensor,
                    date_from=timezone.now(),
                    date_to=timezone.now(),
                    detected=motion_detected)

                sensor_reading.save()

    return HttpResponse('')


@login_required()
def new_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            try:
                my_new_sensor = form.save()
                UserSensor.objects.get_or_create(user=request.user, sensor=my_new_sensor)
                return HttpResponseRedirect(reverse('MotionSensorServer:sensors'))
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
def get_detections_per_user(request):
    user_sensors = [i.sensor for i in UserSensor.objects.filter(user__exact=request.user)]
    detections = SensorReading.objects.order_by("-date_from")
    detections = [i for i in detections if i.sensor in user_sensors]
    return render_to_response('MotionSensorServer/detections.html', {
        "items": detections
    }, RequestContext(request))

@login_required()
def get_detections_per_sensor(request, sensor_id):
    detections = SensorReading.objects.filter(sensor__exact=sensor_id).order_by("-date_from")
    return render_to_response('MotionSensorServer/detections.html', {
        "items": detections
    }, RequestContext(request))

@login_required
def remove_sensor(request, sensor_id):
    sensor_r = get_object_or_404(Sensor, pk=sensor_id)
    sensor_r.delete()
    return HttpResponseRedirect(reverse('MotionSensorServer:sensors'))

@login_required
def switch_sensor_state(request, sensor_id):
    sensor_r = get_object_or_404(Sensor, pk=sensor_id)

    if sensor_r.activated:
        sensor_r.activated = False
    else:
        sensor_r.activated = True

    sensor_r.save()

    return HttpResponseRedirect(reverse('MotionSensorServer:sensors'))
