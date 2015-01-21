from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    short = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "galleries"

    def __unicode__(self):
        return self.title


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name="image_set", default=1)
    title = models.CharField(max_length=100, default='Untitled')
    picture = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(null=True, blank=True)
    caption = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.title
