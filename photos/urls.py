from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),

	url(r'^logout/$', views.logout_user, name='logout'),
	
	url(r'^random/$', views.random, name='random'),

	url(r'^latest/$', views.latest, name='latest'),

	url(r'^years/$', views.years, name='years'),

	url(r'^years/(?P<year>\d\d\d\d)/$', views.months, name='months'),

	url(r'^years/(?P<year>\d\d\d\d)/(?P<month>\w\w\w)/$', views.photos, name='photos'),
	
	url(r'^years/(?P<year>\d\d\d\d)/(?P<month>\w\w\w)/(?P<title>[-_:.a-zA-Z0-9 ]+)$', views.photo_detail, name='photo_detail'),

]
