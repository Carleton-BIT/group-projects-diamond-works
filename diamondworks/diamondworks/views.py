from django.shortcuts import render

def home(request):
    return render(request, "index.html")

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

def login(request):
    return render(request, "Login.html", {"error": "TEST ERROR"})