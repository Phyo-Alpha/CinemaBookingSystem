# Generated by Django 4.2.1 on 2023-05-18 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_moviesession_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 17, 46, 10, 709288)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='purchased_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 17, 46, 10, 711282)),
        ),
    ]