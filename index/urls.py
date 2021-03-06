from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),

	url(r'^main/$', views.main, name="main"),
	url(r'^main/(?P<sub_id>[0-9]+)/$', views.sub_inf, name="sub_inf"),

	url(r'^log/$', views.login, name="log"),

	url(r'^reg/$', views.reg, name="reg"),

]
