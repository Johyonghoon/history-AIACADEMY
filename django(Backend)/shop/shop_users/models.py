from django.db import models


class ShopUser(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=120, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    passwd = models.CharField(max_length=255)
    point = models.IntegerField()

    class Meta:
        db_table = "shop_users"

    def __str__(self):
        return f"{self.pk} {self.email} {self.nickname} {self.passwd} {self.point}"

