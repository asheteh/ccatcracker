# Generated by Django 2.2.1 on 2019-12-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0005_chord'),
    ]

    operations = [
        migrations.CreateModel(
            name='chor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_names', models.TextField(blank=True)),
                ('sargam', models.TextField(blank=True)),
                ('status', models.CharField(max_length=110)),
                ('url', models.CharField(default='old', max_length=300)),
            ],
        ),
    ]