from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),

	url(r'^main/$', views.main, name="main"),

	url(r'^log/$', views.login, name="login"),

	url(r'^reg/$', views.reg, name="reg"),

]
