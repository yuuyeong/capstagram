from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import View


class UserSignIn(View):
    def get(self, request):
        return render(
            request,
            "users/signin.html",
            context={},
        )

    def post(self, request):
        # inputed_id = request.POST.get("my_id")
        # inputed_pw = request.POST.get("my_pw")
        # next_page = request.POST.get("my_url")

        # user = authenticate(
        #     username=inputed_id,
        #     password=inputed_pw,
        # )

        # if user:
        #     login(request, user)
        #     return redirect(next_page)
        # return redirect(reverse("siginin") + "?next=" + next_page)
        pass
