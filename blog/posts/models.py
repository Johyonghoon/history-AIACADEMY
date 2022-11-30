from datetime import datetime

from django.db import models

from blog.blog_users.models import BlogUser


class Post(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user_id = models.ForeignKey(BlogUser, on_delete=models.CASCADE)  # on_delete : PK가 죽으면 FK도 죽는다.

    class Meta:
        db_table = "blog_posts"

    def __str__(self):
        return f"{self.pk} {self.title} {self.context} {self.created_at} {self.updated_at} {self.user_id}"
