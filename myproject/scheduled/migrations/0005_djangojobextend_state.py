# Generated by Django 4.0.6 on 2022-11-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduled', '0004_djangojobextend_crontab'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangojobextend',
            name='state',
            field=models.BooleanField(default=1, verbose_name='是否开启'),
        ),
    ]
