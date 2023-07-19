# Generated by Django 4.1.5 on 2023-01-05 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "user_email",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("user_id", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("user_name", models.CharField(max_length=20)),
                ("phone", models.CharField(max_length=20)),
                ("birth", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=20)),
                ("job", models.CharField(max_length=20)),
                ("user_interests", models.CharField(max_length=20)),
                ("token", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "exrc_users",
            },
        ),
    ]
