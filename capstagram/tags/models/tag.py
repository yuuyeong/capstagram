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

    @property
    def full_name(self):
        return "#{tag_name}".format(
            tag_name=self.name
        )

    def __str__(self):
        return "#{tag_name}".format(
            tag_name=self.name
        )

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
            "tag-detail",
            kwargs={
                "slug": self.name,
            }
        )
