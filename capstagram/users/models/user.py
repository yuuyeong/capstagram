from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    descriptions = models.TextField()

    follower_set = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followee_set",
        through="Follow",
        through_fields=("followee", "follower")
    )
