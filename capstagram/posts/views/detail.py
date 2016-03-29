from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from .list import PostBaseView


class PostDetailView(LoginRequiredMixin, PostBaseView, DetailView):
    template_name = "posts/detail.html"
    context_object_name = "post"
