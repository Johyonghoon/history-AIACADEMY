from django.db import models

from blog.posts.models import Post


class Tag(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_tags"

    def __str__(self):
        return f"{self.pk} {self.title} {self.posts}"


