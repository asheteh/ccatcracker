# Generated by Django 2.2.1 on 2020-03-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200314_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='sargam',
            name='keywords',
            field=models.TextField(blank=True, default='music sargams'),
        ),
        migrations.AddField(
            model_name='sargam',
            name='meta_disc',
            field=models.TextField(blank=True, default='music sargams'),
        ),
        migrations.AddField(
            model_name='sargam',
            name='meta_name',
            field=models.TextField(blank=True, default='music sargams'),
        ),
        migrations.AddField(
            model_name='sargam',
            name='relased',
            field=models.CharField(default='dont-know', max_length=100),
        ),
        migrations.AddField(
            model_name='sargam',
            name='url',
            field=models.TextField(blank=True, default='sd'),
        ),
    ]