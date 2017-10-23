# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20171023_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabeticsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MedicationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('code', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='diabetics_type',
            field=models.IntegerField(null=True, verbose_name=user_profile.models.DiabeticsType, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='diagnosis_year',
            field=models.IntegerField(default=1300),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fasting_blood_sugar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='medication_type',
            field=models.ForeignKey(blank=True, to='user_profile.MedicationType', null=True),
        ),
    ]
