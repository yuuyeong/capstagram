from django.db import models
from django.conf import settings

from tags.models import Tag


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
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    tag_set = models.ManyToManyField(
        Tag,
    )

    like_user_set = models.ManyToManyField(
         settings.AUTH_USER_MODEL,
         related_name="like_post_set",
         through="Like",
    )

    def init_hash_id(self):
        from capstagram.utils.hash_id import get_encoded_hash_id

        self.hash_id = get_encoded_hash_id(self)
        self.save()
