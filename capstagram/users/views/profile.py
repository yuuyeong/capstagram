from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model


class UserProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "users/profile.html"
