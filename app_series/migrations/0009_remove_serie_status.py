# Generated by Django 4.1.5 on 2023-04-05 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_series', '0008_rename_seasons_episode_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='status',
        ),
    ]
