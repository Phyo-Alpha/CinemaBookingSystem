# Generated by Django 4.2.1 on 2023-05-20 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seat',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cinemaroom'),
        ),
        migrations.AddField(
            model_name='seat',
            name='session_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.moviesession'),
        ),
        migrations.AddField(
            model_name='ratingandreview',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
        ),
        migrations.AddField(
            model_name='ratingandreview',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moviesession',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
        ),
        migrations.AddField(
            model_name='moviesession',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cinemaroom'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
