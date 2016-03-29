from django.views.generic import View, ListView

from posts.models import Post


class PostBaseView(View):
    model = Post


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "post_list"
