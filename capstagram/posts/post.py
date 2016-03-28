from django.db import models
from django.conf import settings


class Post(models.Model):
    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )

    image = models.ImageField()
    content = models.TextField()

    created_at = models.DateTimeField(
        auto_add_now=True,
    )

    updated_at = models.DateTimeField(
        auto_add=True,
    )

    def init_hash_id(self):
        from capstagram.utils.hash_id import get_encoded_hash_id

        self.hash_id = get_encoded_hash_id(self)
        self.save()

