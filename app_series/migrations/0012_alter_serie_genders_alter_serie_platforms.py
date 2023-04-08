# Generated by Django 4.1.5 on 2023-04-08 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_series', '0011_alter_serie_genders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='genders',
            field=models.ManyToManyField(related_name='series', to='app_series.gender'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='platforms',
            field=models.ManyToManyField(related_name='series', to='app_series.platform'),
        ),
    ]