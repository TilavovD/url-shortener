from django.db import models


# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=6, unique=True)
    link = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
