# Generated by Django 2.1.5 on 2020-07-16 21:29

import cloudinary.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('ecommerce_app', '0008_remove_product_validation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('sub_title', models.CharField(max_length=127)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('slug', models.SlugField()),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('Validator_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('Validator_name', models.CharField(blank=True, max_length=191, null=True)),
                ('Course_module_file', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file')),
                ('duration', models.CharField(max_length=191)),
                ('category', models.CharField(choices=[('leadership', 'leadership'), ('SDGs', 'SDGs')], default='General Education', max_length=127)),
                ('description', models.TextField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('finish_date', models.DateField(null=True)),
                ('is_official', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('students', models.ManyToManyField(to='account.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ShortCourseLecture',
            fields=[
                ('lecture_id', models.AutoField(primary_key=True, serialize=False)),
                ('lecture_num', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('week_num', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('title', models.CharField(default='', max_length=63, null=True)),
                ('description', models.TextField(default='', null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('vimeo_url', models.URLField(blank=True, null=True)),
                ('bliptv_url', models.URLField(blank=True, null=True)),
                ('preferred_service', models.CharField(choices=[('1', 'YouTube'), ('2', 'Vimeo')], default='1', max_length=1)),
                ('shortcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.ShortCourse')),
            ],
        ),
        migrations.CreateModel(
            name='ShortCourseModules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module_name', models.CharField(max_length=80)),
                ('Module_duration', models.CharField(max_length=191)),
                ('module_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('module_file', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file')),
                ('module_description', models.TextField()),
                ('ShortCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='ecommerce_app.ShortCourse')),
            ],
        ),
    ]