from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()  # ✅ Ensures we reference the correct user model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "display_name", "password1", "password2"]

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")  # ✅ Change to email (since `USERNAME_FIELD = "email"` in the model)

    def clean(self):
        email = self.cleaned_data.get("username")  # `username` maps to `email`
        password = self.cleaned_data.get("password")
        if email and password:
            self.user_cache = authenticate(username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password.")
        return self.cleaned_data
