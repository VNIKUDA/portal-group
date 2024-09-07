from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager

# Create your models here
class UserManager(DefaultUserManager):
    def create_user(self, username: str, email: str | None = ..., password: str | None = ..., **extra_fields: Any) -> Any:
        user = super().create_user(username, email, password, **extra_fields)
        Profile.objects.create(user=user)

        return user
    
    def create_superuser(self, username: str, email: str | None, password: str | None, **extra_fields: Any) -> Any:
        user = super().create_superuser(username, email, password, **extra_fields)
        Profile.objects.create(user=user)

        return user

class User(AbstractUser):
    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username