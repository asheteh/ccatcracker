# Generated by Django 2.2.1 on 2019-08-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_send'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField()),
                ('apti_q', models.TextField(blank=True)),
                ('A', models.TextField(blank=True)),
                ('B', models.TextField(blank=True)),
                ('C', models.TextField(blank=True)),
                ('D', models.TextField(blank=True)),
                ('ans', models.TextField(blank=True)),
            ],
        ),
    ]
