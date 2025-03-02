from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view

urlpatterns = [
    path("", home, name="home"),  # ✅ Ensure this is FIRST so Django picks it up
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls")),  # Course-related pages
    path("users/", include("users.urls")),  # User authentication
    path("payments/", include("payments.urls")),  # Payment handling
]
