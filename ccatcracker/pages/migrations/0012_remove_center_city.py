# Generated by Django 2.2.1 on 2019-10-18 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_ds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='city',
        ),
    ]
