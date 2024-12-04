# Generated by Django 5.1.3 on 2024-11-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_app', '0004_remove_drone_current_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_lat', models.FloatField()),
                ('start_lng', models.FloatField()),
                ('end_lat', models.FloatField()),
                ('end_lng', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Drone',
        ),
    ]
