from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Update with a real view function
]
