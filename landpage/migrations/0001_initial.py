# Generated by Django 2.1.4 on 2020-03-25 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePreview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_filename', models.CharField(max_length=31)),
                ('title', models.CharField(max_length=63)),
                ('sub_title', models.CharField(max_length=127)),
                ('category', models.CharField(max_length=31)),
                ('description', models.TextField()),
                ('summary', models.TextField()),
            ],
            options={
                'db_table': 'at_course_previews',
            },
        ),
        migrations.CreateModel(
            name='LandpageContactMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=63)),
                ('message', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'at_landpage_contact_message',
            },
        ),
        migrations.CreateModel(
            name='LandpageCoursePreview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_filename', models.CharField(max_length=31)),
                ('title', models.CharField(max_length=127)),
                ('category', models.CharField(max_length=31)),
            ],
            options={
                'db_table': 'at_landpage_course_previews',
            },
        ),
        migrations.CreateModel(
            name='LandpagePartner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_filename', models.CharField(max_length=31)),
                ('title', models.CharField(max_length=127)),
                ('url', models.URLField()),
            ],
            options={
                'db_table': 'at_landpage_partners',
            },
        ),
        migrations.CreateModel(
            name='LandpageTeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=31)),
                ('role', models.CharField(max_length=31)),
                ('twitter_url', models.CharField(max_length=255, null=True)),
                ('facebook_url', models.CharField(max_length=255, null=True)),
                ('image_filename', models.CharField(max_length=255, null=True)),
                ('linkedin_url', models.CharField(max_length=255, null=True)),
                ('github_url', models.CharField(max_length=255, null=True)),
                ('google_url', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'db_table': 'at_landpage_team_members',
            },
        ),
        migrations.CreateModel(
            name='LandpageTopPickCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'at_landpage_top_pick_courses',
            },
        ),
    ]
