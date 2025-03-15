from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart

app_name = "cart"

urlpatterns = [
    path("", cart_detail, name="cart_detail"),
    path("add/<int:course_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_id>/", remove_from_cart, name="remove_from_cart"),
]
