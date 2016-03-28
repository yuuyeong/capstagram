from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    name = "Posts"

    def ready(self):
        from posts.signals.post_save import post_save_post

