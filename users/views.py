from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

User = get_user_model()  # ✅ Ensure correct user model reference

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
            return redirect("home")
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
            user = form.get_user()  # ✅ Get authenticated user
            login(request, user)
            messages.success(request, f"Welcome back, {user.email}!")

            # ✅ Redirect to 'next' if available, otherwise go home
            next_url = request.GET.get("next") or "home"
            return redirect(next_url)
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = CustomAuthenticationForm()

    return render(request, "users/signin.html", {"form": form})

@login_required
def signout_view(request):
    """Handles user logout."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")
