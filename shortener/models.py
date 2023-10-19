from django.db import models


# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
