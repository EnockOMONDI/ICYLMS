# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='bio',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='interests',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='/profile_pic'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
