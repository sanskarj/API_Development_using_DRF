# Generated by Django 3.0.6 on 2020-05-21 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0010_auto_20200520_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievements',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='users',
            new_name='user',
        ),
    ]
