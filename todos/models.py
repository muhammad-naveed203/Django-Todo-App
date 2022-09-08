from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    dsec = models.CharField(max_length=220)

    def __str__(self):
        return self.title


class TodoList(models.Model):
    PRIVACY_CHOICES = (
        ('public', 'PUBLIC'),
        ('private', 'PRIVATE'),
    )

    # item = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    privacy = models.CharField(max_length=7, choices=PRIVACY_CHOICES)

    def __str__(self):
        return self.title
