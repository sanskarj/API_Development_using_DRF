# Generated by Django 3.0.6 on 2020-06-16 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0026_blog_certification_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
