# Generated by Django 4.1.7 on 2023-04-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0011_auto_20200709_1431'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ID_Card',
        ),
        migrations.RemoveField(
            model_name='service_man',
            name='id_card',
        ),
        migrations.AddField(
            model_name='service_man',
            name='service_charge',
            field=models.BigIntegerField(default=500),
        ),
    ]