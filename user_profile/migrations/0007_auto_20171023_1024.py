# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20171023_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='code',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gender',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]
