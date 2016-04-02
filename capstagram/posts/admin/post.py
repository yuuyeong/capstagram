from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass
