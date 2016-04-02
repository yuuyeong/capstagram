from django.views.generic import DetailView

from tags.models import Tag


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"
    slug_field = "name"
