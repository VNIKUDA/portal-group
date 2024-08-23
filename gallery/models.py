from django.db import models
from django.contrib.auth import get_user_model

class Media(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('photo', 'Фото'),
        ('video', 'Відео'),
    )

    title = models.CharField(max_length=100)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='media/')
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title