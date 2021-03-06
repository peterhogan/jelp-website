# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('photo_name', models.CharField(max_length=100)),
                ('date_taken', models.DateField()),
                ('photo_path', models.CharField(max_length=200)),
            ],
        ),
    ]
