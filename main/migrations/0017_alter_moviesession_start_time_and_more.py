# Generated by Django 4.2 on 2023-05-14 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_foodanddrinks_ticket_is_paid_ticket_purchased_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 17, 2, 47, 472337)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='purchased_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 17, 2, 47, 475247)),
        ),
    ]
