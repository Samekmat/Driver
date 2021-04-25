from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    training = models.ForeignKey('Training', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Training(models.Model):
    question = models.ManyToManyField(Question)
