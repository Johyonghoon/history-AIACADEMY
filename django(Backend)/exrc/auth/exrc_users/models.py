from django.db import models


class Users(models.Model):
    use_in_migrations = True
    user_id = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birth = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    user_interests = models.CharField(max_length=20)
    token = models.CharField(max_length=20)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    class Meta:
        db_table = "exrc_users"

    def __str__(self):
        return f"{self.pk} {self.user_email} {self.password} {self.user_name} {self.phone} {self.birth} " \
               f"{self.address} {self.job} {self.user_interests} {self.token}"

