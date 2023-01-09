from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom User Model"""
    name = models.CharField(null=True, blank=True, max_length=100)
