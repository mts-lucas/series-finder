# Generated by Django 4.1.5 on 2023-04-05 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_series', '0007_rename_season_episode_seasons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='seasons',
            new_name='season',
        ),
    ]
