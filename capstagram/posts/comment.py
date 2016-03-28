from django.conf import settings
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )

    post = models.ForeignKey(
        "Post"
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_add_now=True,
    )

    updated_at = models.DateTimeField(
        auto_add=True,
    )