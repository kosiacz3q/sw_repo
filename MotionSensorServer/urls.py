from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^motion/reading/([0-9]{4})/([0-1])/$', views.reading),
    url(r'^motion/new_sensor/', views.new_sensor, name='new_sensor'),
    url(r'^motion/sensors/(?P<sensor_id>[0-9]+)/remove/', views.remove_sensor, name='remove_sensor'),
    url(r'^motion/sensors/', views.get_sensors, name='sensors'),
    url(r'^motion/detections/', views.get_detections, name='detections'),
    url(r'^motion/detections/', views.get_detections, name='detections')
]
