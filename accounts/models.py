from django.contrib.auth.models import AbstractUser

from django.db import models

import uuid

class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_seller = models.BooleanField(default=False)

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "is_seller",
    ]
