from django.shortcuts import render, redirect
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")
def homepage(request):
    return render(request, "homepage.html")
def signup(request):
    context = {}

    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Only allow Carleton email
        if not email.endswith("@cmail.carleton.ca"):
            context["error"] = "You must use your Carleton email address."

        # Check if passwords match
        elif password != confirm_password:
            context["error"] = "Passwords do not match."

        else:
            context["success"] = "Account created successfully!"

    return render(request, "signup.html", context)

def forgot_password(request):
    context = {}

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()

        if not email.endswith("@cmail.carleton.ca"):
            context["error"] = "Only Carleton emails are allowed."
        else:
            context["success"] = "If this email exists, a reset link was sent."

    return render(request, "forgot_password.html", context)