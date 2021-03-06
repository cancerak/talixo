# Generated by Django 2.2 on 2019-05-15 13:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('economy', 'Economy class'), ('business', 'Business class'), ('first', 'First class')], max_length=8)),
                ('engine', models.CharField(choices=[('normal', 'Combustion engine'), ('hybrid', 'Hybrid engine'), ('electric', 'Electric engine')], max_length=8)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('passengers', models.PositiveIntegerField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=10, unique=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2019)])),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.CarModel')),
            ],
        ),
    ]
