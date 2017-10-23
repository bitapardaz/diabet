# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_remove_userprofile_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='registration_path',
            field=models.ForeignKey(blank=True, to='user_profile.RegistrationPath', null=True),
        ),
    ]
