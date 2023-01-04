from django.db import models


class BlogUser(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=120, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    passwd = models.CharField(max_length=255)

    class Meta:
        db_table = "blog_users"

    def __str__(self):
        return f"{self.pk} {self.email} {self.nickname} {self.passwd}"

