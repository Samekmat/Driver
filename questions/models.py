from django.db import models


class Question(models.Model):
    content = models.CharField(max_length=200)
    training = models.ForeignKey('Training', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Training(models.Model):
    question = models.ManyToManyField(Question)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
