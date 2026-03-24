from django.shortcuts import render
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required

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

        if not email.endswith("@cmail.carleton.ca"):
            context["error"] = "You must use your Carleton email address."
        elif password != confirm_password:
            context["error"] = "Passwords do not match."
        else:
            request.session["fullname"] = fullname
            request.session["email"] = email
            request.session["password"] = password
            request.session["phone"] = request.session.get("phone", "")
            request.session["gender"] = request.session.get("gender", "")
            messages.success(request, "Account created successfully!")
            return redirect("homepage")

    return render(request, "signup.html", context)

def login(request):
    context = {}

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        saved_email = request.session.get("email")
        saved_password = request.session.get("password")

        if not email.endswith("@cmail.carleton.ca"):
            context["error"] = "Only Carleton emails are allowed."
        elif saved_email and saved_password:
            if email == saved_email and password == saved_password:
                messages.success(request, "You are now logged in.")
                return redirect("homepage")
            else:
                context["error"] = "Incorrect email or password."
        else:
            request.session["email"] = email
            request.session["fullname"] = request.session.get("fullname", "CU-Eats User")
            request.session["password"] = password
            request.session["phone"] = request.session.get("phone", "")
            request.session["gender"] = request.session.get("gender", "")
            messages.success(request, "You are now logged in.")
            return redirect("homepage")

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

def account(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname", "").strip()
        phone = request.POST.get("phone", "").strip()
        gender = request.POST.get("gender", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        request.session["fullname"] = fullname
        request.session["phone"] = phone
        request.session["gender"] = gender

        if password or confirm_password:
            if password == confirm_password:
                request.session["password"] = password
                messages.success(request, "Changes saved successfully.")
            else:
                messages.error(request, "Passwords do not match.")
                return redirect("account")
        else:
            messages.success(request, "Changes saved successfully.")

        return redirect("account")

    context = {
        "fullname": request.session.get("fullname", ""),
        "email": request.session.get("email", ""),
        "phone": request.session.get("phone", ""),
        "gender": request.session.get("gender", ""),
    }

    return render(request, "account.html", context)