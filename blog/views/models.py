from django.db import models
from django.utils import timezone

from blog.blog_users.models import BlogUser
from blog.posts.models import Post


class View(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=15)
    created_at = models.DateField(default=timezone.now)

    user_id = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_views"

    def __str__(self):
        return f"{self.pk} {self.ip_address} {self.created_at} {self.user_id} {self.post_id}"
