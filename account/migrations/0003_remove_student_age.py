# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191228_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
