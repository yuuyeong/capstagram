from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return "#{tag_name}".format(
            tag_name=self.name
        )
