# Generated by Django 2.2.1 on 2020-04-22 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_sargams_youtube'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sargams',
            name='youtube',
        ),
    ]
