# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0002_auto_20150714_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='valid_until',
            field=models.DateTimeField(verbose_name='valid until', default=datetime.datetime(2015, 7, 17, 15, 44, 55, 285318, tzinfo=utc)),
        ),
    ]
