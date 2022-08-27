# Generated by Django 4.0.3 on 2022-03-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appetizerItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Appetizers',
            },
        ),
        migrations.CreateModel(
            name='baoItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Baos',
            },
        ),
        migrations.CreateModel(
            name='dessertItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Desserts',
            },
        ),
        migrations.CreateModel(
            name='dimsumItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Dim Sum',
            },
        ),
        migrations.CreateModel(
            name='drinkItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Drinks',
            },
        ),
        migrations.CreateModel(
            name='noodleSoupItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Noodle Soups',
            },
        ),
        migrations.CreateModel(
            name='sushiItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Sushi',
            },
        ),
    ]
