# Generated by Django 4.1.3 on 2022-11-30 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theaters', '0001_initial'),
        ('showtimes', '0001_initial'),
        ('movie_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheaterTicket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('movie_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_users.movieuser')),
                ('showtime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showtimes.showtime')),
                ('theater_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theaters.theater')),
            ],
            options={
                'db_table': 'movie_theater_tickets',
            },
        ),
    ]
