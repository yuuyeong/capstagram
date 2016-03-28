from django.db import models
from django.conf import settings


class Post(models.Model):
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

