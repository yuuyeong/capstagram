from django.views.generic import CreateView


class CommentCreateView(LoginRequiredMixin, CreateView):
    # 모델 넣어주는 거 잊지 말고!
    model = Comment
    fields = ['content']

    # form은 comment의 content 정보만을 가지고 있으므로
    # user & post 정보를 넣어주어 form.instance를 완성시킨다.
    # form.instance를 모델에 저장하고 redirect abs_url
    def form_valid(self, form):
        form.instance.user = self.request.user
        # 글 번호를 가져오는 법!
        # from IPython import embed; embed()
        form.instance.post = Post.objects.get(
            pk=self.kwargs.get('pk')
        )
        return super(CommentCreateView, self).form_valid(form)
