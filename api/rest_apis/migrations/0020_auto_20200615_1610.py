# Generated by Django 3.0.6 on 2020-06-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0019_auto_20200605_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimage',
            name='user',
        ),
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Imageupload',
        ),
        migrations.DeleteModel(
            name='profileimage',
        ),
    ]
