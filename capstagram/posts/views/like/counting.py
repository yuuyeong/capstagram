from django.shortcuts import redirect
from django.views.generic import View

from posts.models import Like, Post


class LikeCountView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(hash_id=kwargs.get("slug"))

        like, is_created = Like.objects.get_or_create(
            user=user,
            post=post,
        )

        # 이미 좋아요를 누른 상태라면 삭제한다.
        if not is_created:
            like.delete()

        return redirect(post)
