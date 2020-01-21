# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0002_auto_20150509_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=cloudinary.models.CloudinaryField(verbose_name='image', max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=cloudinary.models.CloudinaryField(verbose_name='fileupload', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='file',
            field=cloudinary.models.CloudinaryField(verbose_name='policyfiles', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='file',
            field=cloudinary.models.CloudinaryField(verbose_name='syllabusfiles', max_length=255, null=True),
        ),
    ]
