from django.db import models # type: ignore

class AlbumCategory(models.Model):
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='albums/')

class Photo(models.Model):
    album = models.ForeignKey(AlbumCategory, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
