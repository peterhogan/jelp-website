from django.conf.urls import url
from . import views

urlpatterns = [
	# /login/
	url(r'^$', views.login_user, name='login'),
]
