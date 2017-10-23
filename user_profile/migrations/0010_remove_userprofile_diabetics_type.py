# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_auto_20171023_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='diabetics_type',
        ),
    ]
