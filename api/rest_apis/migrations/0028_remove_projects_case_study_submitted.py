# Generated by Django 3.0.6 on 2020-06-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0027_auto_20200616_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='case_study_submitted',
        ),
    ]