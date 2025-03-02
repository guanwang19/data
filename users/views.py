from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

User = get_user_model()  # ✅ Get the custom user model

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # ✅ Automatically activate user
            user.save()
            login(request, user)
            return redirect("home")  # ✅ Ensure 'home' exists in urls.py
    else:
        form = CustomUserCreationForm()

    return render(request, "users/signup.html", {"form": form})

def signin_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # ✅ Get the authenticated user
            login(request, user)
            return redirect("home")  # ✅ Ensure 'home' exists in urls.py
    else:
        form = CustomAuthenticationForm()

    return render(request, "users/signin.html", {"form": form})

@login_required
def signout_view(request):
    logout(request)
    return redirect("home")  # ✅ Redirect to home after logout

