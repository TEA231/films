from django.db import models

class Films(models.Model):
    cover = models.FileField(upload_to="films/covers/")
    video = models.FileField(upload_to="films/video/")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)


class Comments(models.Model):
    text = models.TextField(blank=True)
    key = models.ForeignKey('Films', on_delete=models.CASCADE)
