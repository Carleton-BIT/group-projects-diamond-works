from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("home")


def home(request):
    return render(request, "index.html")


def homepage(request):
    return render(request, "homepage.html")


def signup(request):
    context = {}

    if request.method == "POST":
        fullname = request.POST.get("fullname", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        username = email.split("@")[0] if email else ""

        if not email or not email.endswith("@cmail.carleton.ca"):
            context["error"] = "You must use your Carleton email address."

        elif password != confirm_password:
            context["error"] = "Passwords do not match."

        elif User.objects.filter(username=username).exists():
            context["error"] = "That username already exists."

        elif User.objects.filter(email=email).exists():
            context["error"] = "That email is already in use."

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("login")

    return render(request, "signup.html", context)


def login_view(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("homepage")
        else:
            context["error"] = "Invalid username or password."
            
    return render(request, "login.html", context)

def forgot_password(request):
    context = {}

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()

        if not email.endswith("@cmail.carleton.ca"):
            context["error"] = "Only Carleton emails are allowed."
        else:
            context["success"] = "If this email exists, a reset link was sent."

    return render(request, "forgot_password.html", context)


def about(request):
    return render(request, "aboutus.html")


def support(request):
    return render(request, "supportpage.html")