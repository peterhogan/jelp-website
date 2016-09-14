# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150717_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='date_taken',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo_name',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo_path',
        ),
        migrations.AddField(
            model_name='photo',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 7, 21, 17, 21, 35, 392486, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 17, 21, 43, 294438, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='orientation',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='path',
            field=models.FilePathField(allow_folders=True, default='/home/pine/python/django/mysite2/photos/static/photos', path='/home/pine/python/django/mysite2/photos/static/photos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2015, 7, 21, 17, 22, 40, 92641, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
