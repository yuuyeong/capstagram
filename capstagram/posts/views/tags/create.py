from django.shortcuts import redirect
from django.views.generic import View

from posts.models import Post
from tags.models import Tag


class TagCreateView(View):
    def post(self, request, *args, **kwargs):
        inputed_name = request.POST.get("name")
        retrieved_post = Post.objects.get(
            hash_id=self.kwargs.get("slug")
        )

        tag, is_tag_created = Tag.objects.get_or_create(
            name=inputed_name,
        )
        retrieved_post.tag_set.add(tag)

        return redirect(retrieved_post)
