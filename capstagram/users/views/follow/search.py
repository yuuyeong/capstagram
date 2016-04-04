from django.views.generic import ListView

from django.contrib.auth import get_user_model


class UserListView(ListView):
    model = get_user_model()
    template_name = "users/search.html"
    context_object_name = "user_list"

    def get_queryset(self):
        users = super(UserListView, self).get_queryset()
        # 나를 제외한 모든 사용자 목록
        users = users.exclude(
            username=self.request.user.username,
        )

        # 내가 팔로우 하지 않는 사용자 목록
        users = users.exclude(
            id__in=self.request.user.follower_set.all(),
        )
        return users
