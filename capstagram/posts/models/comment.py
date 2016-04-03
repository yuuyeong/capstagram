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
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
            "detail",
            kwargs={
                "slug": self.post.hash_id,
            }
        )
