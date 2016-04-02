from django.contrib import admin

from posts.models import Comment


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass
