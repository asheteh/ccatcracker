# Generated by Django 2.2.1 on 2020-03-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_sargams_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='sargams',
            name='keywords',
            field=models.TextField(blank=True, default='music sargams'),
        ),
        migrations.AddField(
            model_name='sargams',
            name='meta_disc',
            field=models.TextField(blank=True, default='music sargams'),
        ),
        migrations.AddField(
            model_name='sargams',
            name='meta_name',
            field=models.TextField(blank=True, default='music sargams'),
        ),
        migrations.AddField(
            model_name='sargams',
            name='relased',
            field=models.CharField(default='dont-know', max_length=100),
        ),
    ]
