from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email', **NULLABLE)
    phone = models.CharField(unique=True, max_length=35, verbose_name='phone', **NULLABLE)
    telegram_id = models.CharField(unique=True, max_length=35, verbose_name="Telegram ID", **NULLABLE)
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
