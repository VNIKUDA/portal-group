from django.db import models
from django.contrib.auth import get_user_model

class Thread(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'Post by {self.created_by.username} on {self.thread.title}'
