# Generated by Django 2.2.1 on 2019-10-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTest', '0003_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField()),
                ('question', models.TextField(blank=True)),
                ('a', models.TextField(blank=True)),
                ('b', models.TextField(blank=True)),
                ('c', models.TextField(blank=True)),
                ('d', models.TextField(blank=True)),
                ('ans', models.TextField(blank=True)),
                ('qtype', models.CharField(max_length=40)),
            ],
        ),
    ]
