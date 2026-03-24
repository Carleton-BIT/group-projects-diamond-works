from django.contrib import admin
from django.urls import path, include
from .views import home, homepage, signup, login, forgot_password, account

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("homepage/", homepage, name="homepage"),
    path("signup/", signup, name="signup"),
    #path("accounts/login/", login, name="login"),
    path("forgot-password/", forgot_password, name="forgot_password"),

    path("account/", account, name="account"),
    path('accounts/', include('django.contrib.auth.urls')),
]
