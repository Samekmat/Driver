from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=120, null=True)
    content = models.CharField(max_length=200)
    training = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='question_training', null=True)

    def __str__(self):
        return self.name


class Training(models.Model):
    name = models.CharField(max_length=120, null=True)
    question = models.ManyToManyField(Question, related_name='exercise')

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Advice(models.Model):
    name = models.CharField(max_length=200)
    multimedia = models.FileField(upload_to='questions/multimedia', null=True)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
