from ast import mod
from django.contrib.auth.models import AbstractUser

from django.db import models


class Account(AbstractUser):
    is_seller = models.BooleanField(default=False)

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "is_seller",
    ]
