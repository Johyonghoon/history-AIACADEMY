from django.db import models

from movie.movie_users.models import MovieUser
from movie.movies.models import Movie
from movie.theaters.models import Theater


class Showtime(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    cinema_id = models.ForeignKey(MovieUser, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater_id = models.ForeignKey(Theater, on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_showtimes"

    def __str__(self):
        return f"{self.pk} {self.start_time} {self.end_time} {self.cinema_id} {self.movie_id} {self.theater_id}"

