from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)

class Room(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)

class Film(models.Model):
    title = models.CharField(max_length=120)
    poster = ProcessedImageField(upload_to='images/posters/',
                                 processors=[ResizeToFill(562, 800)],
                                 format='JPEG',
                                 options={'quality': 75})

    def __str__(self):
        return str(self.title)

class Session(models.Model):
    time = models.TimeField(auto_now=False)
    price = models.IntegerField(default=150)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.time)[:5] + '; ' + str(self.price) + 'р.'

class FilmGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)