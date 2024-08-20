from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    TYPE_CHOICES = (
        ("single", "Одна вірна відповідь"),
        {"multiple", "Багато вірних відповідей"}
    )

    text = models.CharField(max_length=150)
    type = models.CharField(choices=TYPE_CHOICES, max_length=25)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")


class Option(models.Model):
    value = models.CharField(max_length=150)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")

    users = models.ManyToManyField(get_user_model(), blank=True)