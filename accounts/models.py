from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse


class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.username}"

    @staticmethod
    def get_absolute_url():
        return reverse("login")
