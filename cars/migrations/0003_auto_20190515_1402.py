# Generated by Django 2.2 on 2019-05-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20190515_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together=set(),
        ),
    ]