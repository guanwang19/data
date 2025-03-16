from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def signup_view(request):
    """Handles user sign-up."""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # ✅ Automatically activate user
            user.save()
            login(request, user)
            messages.success(request, "Account created successfully! You are now logged in.")
            return redirect("courses:course_list")  # ✅ Redirect to courses after signup
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, "users/signup.html", {"form": form})

def signin_view(request):
    """Handles user sign-in."""
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # ✅ Get the authenticated user
            login(request, user)
            messages.success(request, f"Welcome back, {user.email}!")

            # ✅ Redirect to courses after login
            return redirect("courses:course_list")  # ✅ Make sure this name exists in courses/urls.py

        else:
            messages.error(request, "Invalid email or password.")

    else:
        form = CustomAuthenticationForm()

    return render(request, "users/signin.html", {"form": form})

def signout_view(request):
    """Logs out the user."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")  # ✅ Redirect to homepage after logout
