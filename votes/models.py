from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    question = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    

class Option(models.Model):
    value = models.CharField(max_length=150)
    vote = models.ForeignKey(Vote, on_delete=models.Case, related_name="options")

    users = models.ManyToManyField(get_user_model(), blank=True, related_name="chosed_votes_options")