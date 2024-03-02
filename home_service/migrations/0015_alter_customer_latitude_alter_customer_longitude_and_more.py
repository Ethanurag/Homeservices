# Generated by Django 5.0.2 on 2024-02-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0014_customer_latitude_customer_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='latitude',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='customer',
            name='longitude',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='service_man',
            name='latitude',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='service_man',
            name='longitude',
            field=models.DecimalField(decimal_places=9, default=0.0, max_digits=9),
        ),
    ]