# Generated by Django 3.0.6 on 2020-06-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0017_remove_hobby_hobby_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='proficiency',
        ),
        migrations.AddField(
            model_name='skills',
            name='competancy',
            field=models.CharField(default='beginner', max_length=32),
            preserve_default=False,
        ),
    ]