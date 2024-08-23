from django.db import models
from django.contrib.auth import get_user_model


class Mark(models.Model):
    student = models.CharField(max_length=200)
    description = models.TextField()
    logiks = models.TextField(max_length=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.student.username}  - {self.logiks}"
