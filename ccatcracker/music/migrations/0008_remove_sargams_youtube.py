# Generated by Django 2.2.1 on 2020-04-22 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20200422_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sargams',
            name='youtube',
        ),
    ]