from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls", namespace="courses")),
    path("users/", include("users.urls", namespace="users")),
    path("payments/", include("payments.urls", namespace="payments")),
    path("cart/", include("cart.urls", namespace="cart")),
]

# ✅ Serve video files in development
if settings.DEBUG:
    urlpatterns += static("/videos/", document_root="videos/")
