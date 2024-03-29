# Generated by Django 5.0.2 on 2024-02-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0013_service_man_latitude_service_man_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='latitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='customer',
            name='longitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=9),
        ),
    ]
