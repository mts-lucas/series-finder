# Generated by Django 4.1.5 on 2023-04-05 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_series', '0006_alter_serie_genders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='season',
            new_name='seasons',
        ),
    ]
