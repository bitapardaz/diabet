# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_remove_userprofile_diabetics_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='diabetics_type',
            field=models.ForeignKey(blank=True, to='user_profile.DiabeticsType', null=True),
        ),
    ]
