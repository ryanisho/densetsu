# Generated by Django 4.0.3 on 2022-03-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_reservations_phone_alter_reservations_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='date',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
