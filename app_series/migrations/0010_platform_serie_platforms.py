# Generated by Django 4.1.5 on 2023-04-06 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_series', '0009_remove_serie_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='serie',
            name='platforms',
            field=models.ManyToManyField(related_name='platforms', to='app_series.platform'),
        ),
    ]
