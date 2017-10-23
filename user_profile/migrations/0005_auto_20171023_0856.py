# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20171023_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.ForeignKey(blank=True, to='user_profile.Education', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.ForeignKey(blank=True, to='user_profile.Gender', null=True),
        ),
    ]
