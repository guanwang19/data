from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view

urlpatterns = [
    path("", home, name="home"),  # ✅ Ensure this is FIRST so Django picks it up
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls", namespace="courses")),  # ✅ Add namespace
    path("users/", include("users.urls", namespace="users")),  # ✅ Add namespace
    path("payments/", include("payments.urls", namespace="payments")),  # ✅ Add namespace
    path("cart/", include("cart.urls", namespace="cart")),  # ✅ Add namespace
]
