# Generated by Django 5.1.3 on 2024-11-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_app', '0002_drone_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='current_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drone',
            name='current_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
