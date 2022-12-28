from django.db import models

from movie.movie_users.models import MovieUser
from movie.showtimes.models import Showtime
from movie.theaters.models import Theater


class TheaterTicket(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    x = models.IntegerField()
    y = models.IntegerField()

    showtime_id = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    theater_id = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movie_user_id = models.ForeignKey(MovieUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_theater_tickets"

    def __str__(self):
        return f"{self.pk} {self.x} {self.y} {self.showtime_id} {self.theater_id}"

