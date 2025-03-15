from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, signin_view, signout_view

app_name = "users"  # ✅ Ensure namespace is set

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("signin/", signin_view, name="signin"),
    path("signout/", signout_view, name="signout"),

    # ✅ Fix: Ensure success_url uses namespace correctly
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="users/password_reset.html",
        email_template_name="users/password_reset_email.html",
        success_url="/users/password_reset/done/"  # ✅ Explicit absolute path
    ), name="password_reset"),

    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="users/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html"
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="users/password_reset_complete.html"
    ), name="password_reset_complete"),
]
