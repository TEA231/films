from django.db import models

class Films(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    cover = models.ImageField(upload_to="films/covers/")
    video = models.ImageField(upload_to="films/video/")

    def __str__(self):
        return self.name    