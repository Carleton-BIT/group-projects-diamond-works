""""
URL configuration for diamondworks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (home,homepage,signup,login_view, logout_view,forgot_password,about,support,account, wendys,dominos,
    shawarmapalace,pouletrouge,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("homepage/", homepage, name="homepage"),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("about/", about, name="about"),
    path("support/", support, name="support"),
    path("account/", account, name="account"),
    path("shawarmapalace/", shawarmapalace, name="shawarmapalace"),
    path("wendys/", wendys, name="wendys"),
    path("dominos/", dominos, name="dominos"),
    path("pouletrouge/", pouletrouge, name="pouletrouge"),
]