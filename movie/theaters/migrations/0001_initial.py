# Generated by Django 4.1.3 on 2022-11-30 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
                ('seat', models.IntegerField()),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.cinema')),
            ],
            options={
                'db_table': 'movie_theaters',
            },
        ),
    ]
