from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View


class UserSignIn(View):
    def get(self, request):
        return render(
            request,
            "users/login.html",
            context={},
        )

    def post(self, request):
        inputed_id = request.POST.get("my_id")
        inputed_pw = request.POST.get("my_pw")
        next_page = reverse("home")

        user = authenticate(
            username=inputed_id,
            password=inputed_pw,
        )

        if user:
            login(request, user)
            return redirect(next_page)
        return redirect(reverse("signin"))
