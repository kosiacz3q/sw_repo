from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reading/([0-9]{4})/([0-1])/$', views.reading),
    url(r'^new_sensor/', views.new_sensor, name='new_sensor'),
    url(r'^(?P<sensor_id>[0-9]+)/remove/', views.remove_sensor, name='remove_sensor'),
    url(r'^sensors/$', views.get_sensors, name='sensors'),
    url(r'^detections/(?P<sensor_id>[0-9]+)', views.get_detections_per_sensor, name='detections_sensor'),
    url(r'^detections/', views.get_detections_per_user, name='detections_user'),
    url(r'^sensors/(?P<sensor_id>[0-9]+)/switch_sensor_state/', views.switch_sensor_state, name='switch_sensor_state'),
]
