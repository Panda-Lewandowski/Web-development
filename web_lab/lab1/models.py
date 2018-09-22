from django.db import models

class Todo(models.Model):
    task = models.TextField(max_length=150)
    deadline = models.DateTimeField()

