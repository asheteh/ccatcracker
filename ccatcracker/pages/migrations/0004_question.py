# Generated by Django 2.2.1 on 2019-08-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190813_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField()),
                ('task', models.TextField(blank=True)),
                ('ans', models.TextField(blank=True)),
                ('inp', models.TextField(blank=True)),
                ('out', models.TextField(blank=True)),
            ],
        ),
    ]