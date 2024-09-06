from django.db import models
from django.contrib.auth.models import User

class PortfolioItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to='portfolio/screenshots/')
    link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='portfolio/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-created_at"]