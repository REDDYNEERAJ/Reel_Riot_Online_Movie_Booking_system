from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    poster_img = models.ImageField(upload_to='posters/')
    rating = models.FloatField()
    runtime_minutes = models.IntegerField()
    locations = models.ManyToManyField(Location)  # locations where movie is available

    def __str__(self):
        return self.name

class Theatre(models.Model):
    name = models.CharField(max_length=100)
    locations = models.ManyToManyField(Location, related_name='theatres')
    movies = models.ManyToManyField(Movie, related_name='theatres')
    total_seats = models.IntegerField()
    total_rows = models.IntegerField(default=10)   # e.g. 10 rows
    seats_per_row = models.IntegerField(default=20)

    def __str__(self):
        return self.name

class Show(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name='shows')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    show_time = models.TimeField()

    def __str__(self):
        return f"{self.movie.name} at {self.theatre.name} - {self.show_time}"
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    show = models.ForeignKey('Show', on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)  # e.g., A1, B5, etc.
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seat_number} - {self.user.username} - {self.show}"
