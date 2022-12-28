from django.db import models


class Movie(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    director = models.CharField(max_length=20)
    description = models.TextField()
    poster_url = models.TextField()
    running_time = models.IntegerField()
    age_rating = models.IntegerField()

    class Meta:
        db_table = "movie_movies"

    def __str__(self):
        return f"{self.pk}{self.title}{self.director}{self.description}{self.poster_url}{self.running_time}{self.age_rating}"
