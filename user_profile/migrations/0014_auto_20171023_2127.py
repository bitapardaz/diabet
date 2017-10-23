# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0013_auto_20171023_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuestionareItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(to='user_profile.Question')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userquestionare',
            name='question',
        ),
        migrations.RemoveField(
            model_name='userquestionare',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserQuestionare',
        ),
    ]
