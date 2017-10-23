# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_question_userquestionare'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='front_end_short_code',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
