# Generated by Django 2.2.1 on 2019-11-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTest', '0012_remove_test_1_qno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField(blank=True, default=1)),
                ('username', models.CharField(blank=True, max_length=120, unique=True)),
                ('score', models.IntegerField(default=0)),
                ('marks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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