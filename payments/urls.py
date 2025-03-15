from django.urls import path
from .views import checkout, payment_summary, download_invoice

app_name = "payments"

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("summary/", payment_summary, name="payment_summary"),
    path("invoice/<int:payment_id>/", download_invoice, name="download_invoice"),
]
