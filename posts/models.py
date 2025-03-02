from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, blank=True)

    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%M/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now=True, db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =  slugify(self.title)
        super(Image, self).save(*args, **kwargs)
