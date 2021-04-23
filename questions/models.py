from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title
