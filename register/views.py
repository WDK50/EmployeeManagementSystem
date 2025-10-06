from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect("login")  # redirect to login after signup
        else:
            print(form.errors)  # <-- DEBUG
    else:
        form = SignupForm()
    return render(request, "register/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("employee_list")   # redirect to employee list page
    else:
        form = LoginForm()
    return render(request, "register/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")   # back to login after logout
