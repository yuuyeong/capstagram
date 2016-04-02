"""capstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from capstagram.views import home
from users.views import *
from posts.views import *
from tags.views import *


urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^admin/', admin.site.urls),

    url(r'^signin/$', UserSignIn.as_view(), name="signin"),
    url(r'^signout/$', UserSignOut.as_view(), name="signout"),
    url(r'^signup/$', UserSignUp.as_view(), name="signup"),
    url(r'^auth/(?P<slug>\w+)/$', UserProfileView.as_view(), name="profile"),

    url(r'^posts/$', PostListView.as_view(), name="list"),
    url(r'^posts/create/$', PostCreateView.as_view(), name="create"),
    url(r'^posts/detail/(?P<slug>\w+)/$', PostDetailView.as_view(), name="detail"),

    url(r'^tags/(?P<slug>\w+)/$', TagDetailView.as_view(), name="tag-detail"),
    url(r'^posts/detail/(?P<slug>\w+)/tags/$', TagCreateView.as_view(), name="post-tags"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
