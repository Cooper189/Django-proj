from django.db import models

class MainInfo(models.Model):
    img = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
