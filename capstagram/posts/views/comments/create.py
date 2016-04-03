from django.shortcuts import redirect
from django.views.generic import View

from posts.models import Comment, Post


class CommentCreateView(View):
    def post(self, request, *args, **kwargs):
        inputed_content = request.POST.get("content")
        retrieved_user = request.user
        retrieved_post = Post.objects.get(
            hash_id=kwargs.get("slug")
        )

        comment = Comment.objects.create(
            user=retrieved_user,
            post=retrieved_post,
            content=inputed_content,
        )

        return redirect(comment)
