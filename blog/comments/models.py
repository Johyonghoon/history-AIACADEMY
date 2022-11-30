from django.db import models
from django.utils import timezone

from blog.blog_users.models import BlogUser
from blog.posts.models import Post


class Comment(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    parent_id = models.TextField(null=True)

    user_id = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_comments"

    def __str__(self):
        return f"{self.pk} {self.content} {self.created_at} {self.updated_at} {self.parent_id} {self.user_id} {self.post_id}"

