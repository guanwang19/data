from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view

urlpatterns = [
    path("", home, name="home"),  # ✅ Ensure this is FIRST so Django picks it up
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls", namespace="courses")),  # ✅ Namespaces are valid
    path("users/", include("users.urls", namespace="users")),
    path("payments/", include("payments.urls", namespace="payments")),
    path("cart/", include("cart.urls", namespace="cart")),
]
