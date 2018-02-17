from django.db import models

class News(models.Model):
    newsId = models.CharField(max_length=150)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
