# Generated by Django 4.1.3 on 2022-11-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('passwd', models.CharField(max_length=255)),
                ('create_at', models.DateField()),
                ('rank', models.IntegerField(default=1)),
                ('point', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
