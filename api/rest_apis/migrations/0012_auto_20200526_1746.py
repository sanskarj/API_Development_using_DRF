# Generated by Django 3.0.6 on 2020-05-26 12:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_apis', '0011_auto_20200521_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
        migrations.AddField(
            model_name='projects',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
