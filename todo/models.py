from django.contrib.auth.models import AbstractUser
from django.db import models

class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='tasks')

    def __str__(self):
        return self.content

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
