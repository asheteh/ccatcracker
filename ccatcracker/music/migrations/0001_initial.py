# Generated by Django 2.2.1 on 2019-10-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(blank=True, max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=111)),
                ('notation', models.TextField(blank=True)),
                ('link', models.TextField(blank=True)),
            ],
        ),
    ]
