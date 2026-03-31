from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def logout_view(request):
    auth_logout(request)
    return redirect("home")


def home(request):
    return render(request, "index.html")


@login_required
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
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.first_name = fullname
            user.save()

            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("login")

    return render(request, "signup.html", context)

def login_view(request):
    context = {}

    if request.method == "POST":
        username_input = request.POST.get("username", "").strip().lower()
        password = request.POST.get("password", "")

        if username_input.endswith("@cmail.carleton.ca"):
            username_input = username_input.split("@")[0]

        user = authenticate(request, username=username_input, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Logged in successfully, {user.first_name or user.username}")
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




def wendys(request):
    return render(request, "Wendys.html")

def dominos(request):
    return render(request, "Dominos.html")

def shawarmapalace(request):
    return render(request, "shawarmapalace.html")

def pouletrouge(request):
    return render(request, "pouletrouge.html")

@login_required
def account(request):
    context = {
        "fullname": request.user.first_name,
        "email": request.user.email,
        "phone": "",
        "gender": "",
    }

    if request.method == "POST":
        fullname = request.POST.get("fullname", "").strip()
        phone = request.POST.get("phone", "").strip()
        gender = request.POST.get("gender", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        # update name
        request.user.first_name = fullname
        request.user.save()

        # update password
        if password or confirm_password:
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
            else:
                request.user.set_password(password)
                request.user.save()
                messages.success(request, "Password updated. Please log in again.")
                return redirect("login")
        else:
            messages.success(request, "Account updated successfully.")

        # update context
        context["fullname"] = fullname
        context["phone"] = phone
        context["gender"] = gender

    return render(request, "account.html", context)