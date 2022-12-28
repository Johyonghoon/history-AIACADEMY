from django.db import models


class User(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    passwd = models.CharField(max_length=255)
    create_at = models.DateField()

    rank = models.IntegerField(default=1)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = "Users"

    def __str__(self):
        return f"{self.pk}{self.username}{self.passwd}{self.create_at}{self.rank}{self.point}"

