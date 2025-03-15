from django import forms
from django.contrib.auth import get_user_model, authenticate  # ✅ Add authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()  # ✅ Ensures correct user model reference

class CustomUserCreationForm(UserCreationForm):
    """Custom User Signup Form"""

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "display_name", "password1", "password2"]

class CustomAuthenticationForm(AuthenticationForm):
    """Custom Login Form that uses Email instead of Username"""
    username = forms.EmailField(label="Email")  # ✅ Change username field to email

    def clean(self):
        email = self.cleaned_data.get("username")  # `username` maps to `email`
        password = self.cleaned_data.get("password")
        if email and password:
            self.user_cache = authenticate(username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password.")
        return self.cleaned_data
