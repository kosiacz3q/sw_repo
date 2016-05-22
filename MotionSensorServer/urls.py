from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^motion/reading/([0-9]{4})/([0-1])/$', views.reading),
]