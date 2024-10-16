from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    text = models.CharField(max_length=1024)

    def __str__(self):
        return self.title
