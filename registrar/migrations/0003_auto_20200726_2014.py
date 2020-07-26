# Generated by Django 2.1.5 on 2020-07-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0002_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
