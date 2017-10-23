# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20171023_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='family_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='national_code',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postal_code',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
    ]
