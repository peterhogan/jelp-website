from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', include('login.urls', namespace='login')),
	url(r'^photos/', include('photos.urls', namespace="photos")),
	url(r'^admin/', include(admin.site.urls)),
] 

