from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import View


class UserSignUp(View):
    def get(self, request):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request):
        inputed_id = request.POST.get("user_id")
        inputed_pw = request.POST.get("user_pw")
        inputed_des = request.POST.get("user_des")

        get_user_model().objects.create_user(
            username=inputed_id,
            password=inputed_pw,
            descriptions=inputed_des,
        )

        # 생성 후, 로그인 작업
        user = authenticate(
            username=inputed_id,
            password=inputed_pw,
        )

        if user:
            login(request, user)
            return redirect(reverse("home"))
        return redirect(reverse("signup"))
