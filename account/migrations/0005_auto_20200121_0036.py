# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20191227_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(max_length=127, blank=True, null=True, default='Kenya', choices=[('Algeria', 'Algeria'), ('Angola', 'Angola'), ('Benin', 'Benin'), ('Botswana', 'Botswana'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cape Verde', 'Cape Verde'), ('Cameroon', 'Cameroon'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Comoros', 'Comoros'), ('Congo Democratic Republic', 'Congo Democratic Republic'), ('Congo, Republic of the', 'Congo, Republic of the'), ('Cote dIvoire', 'Cote dIvoire'), ('Djibouti', 'Djibouti'), ('Egypt', 'Egypt'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Ghana', 'Ghana'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Kenya', 'Kenya'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Mali', 'Mali'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Rwanda', 'Rwanda'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Senegal', 'Senegal'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Sudan', 'Sudan'), ('Tanzania', 'Tanzania'), ('Togo', 'Togo'), ('Tunisia', 'Tunisia'), ('Uganda', 'Uganda'), ('Zambia', 'Zambia')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(verbose_name='image', max_length=255, blank=True, null=True),
        ),
    ]
