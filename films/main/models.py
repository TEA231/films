from django.db import models

class Films(models.Model):
    cover = models.FileField(upload_to="films/covers/")
    video = models.FileField(upload_to="films/video/")
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255, verbose_name="Категория")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'


class Comments(models.Model):
    text = models.TextField(blank=True)
    key = models.ForeignKey('Films', on_delete=models.CASCADE, verbose_name="Название фильма")

    class Meta:
        verbose_name='Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ['key', 'id']

    def __str__(self):
        return f"{self.id}: {self.key}" 