# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20171023_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AddField(
            model_name='registrationpath',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]
