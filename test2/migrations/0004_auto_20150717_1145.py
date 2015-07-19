# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0003_question_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='valid_until',
            field=models.DateTimeField(verbose_name='valid until', default=django.utils.timezone.now),
        ),
    ]
