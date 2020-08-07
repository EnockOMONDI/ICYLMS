# Generated by Django 2.1.5 on 2020-07-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0004_remove_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
