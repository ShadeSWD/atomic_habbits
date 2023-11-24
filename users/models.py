from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email', **NULLABLE)
    phone = models.CharField(unique=True, max_length=35, verbose_name='Телефон', **NULLABLE)
    telegram_id = models.CharField(unique=True, max_length=35, verbose_name="ID telegram", **NULLABLE)
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
