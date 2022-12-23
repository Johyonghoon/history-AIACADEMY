from django.db import models

from movie.cinemas.models import Cinema


class Theater(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    seat = models.IntegerField()

    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_theaters"

    def __str__(self):
        return f"{self.pk} {self.title} {self.seat} {self.cinema_id}"

