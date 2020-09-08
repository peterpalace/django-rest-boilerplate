from django.db import models
from django.utils.text import slugify


class Video(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    video = models.FileField(upload_to='videos/')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('created',)
