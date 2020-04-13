# Generated by Django 2.1.4 on 2020-04-13 20:34

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_auto_20200413_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='module_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modules',
            name='module_file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
    ]
