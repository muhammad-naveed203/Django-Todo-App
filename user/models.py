from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    username = models.CharField(max_length=150, unique=True)

    objects = UserManager()

    def __str__(self):
        return self.username
