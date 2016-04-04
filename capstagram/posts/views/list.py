from django.views.generic import View, ListView

from posts.models import Post


class PostBaseView(View):
    model = Post


# API 구현 전, 일단 for문을 이용해 전체 글목록을 가져온다.
class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        post_list = Post.objects.filter(
            user__in=self.request.user.follower_set.all()
        )

        user_list = self.request.user.post_set.all()
        all_list = post_list | user_list
        return all_list
