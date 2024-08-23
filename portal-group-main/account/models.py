from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    # Додаткові параметри аккаунта
    # Задача для Максима

    class Meta:
        verbose_name = "account"