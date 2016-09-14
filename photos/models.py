from django.db import models
import datetime
from django.utils import timezone

from os.path import join
from os.path import basename
from glob import glob

class Photo(models.Model):

	title = models.CharField(max_length=100)
	date_created = models.DateField()
	time_created = models.TimeField()
	datetime_created = models.DateTimeField()
	orientation = models.IntegerField()
	path = models.FilePathField(path="/home/pine/python/django/mysite2/photos/static/photos", allow_folders=True)
	#favourite = models.IntegerField(default=0)

	def month_taken():
		return self.date_created.strftime('%b')

	def year_taken():
		return self.date_created.strftime('%Y')

	def recent_photo():
		return self.date_created >= timezone.now() - datetime.timedelta(days=30) 

	def __str__(self):
		return self.title


# ATTEMPT AT SEEING IMAGES IN ADMIN
#def img_tag(self):
#	return u'<img src=%s />' % self.path
#img_tag.short_description = 'Image'
#img_tag.allow_tags = True
