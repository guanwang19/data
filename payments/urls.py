from django.urls import path
from .views import PaymentListView, PaymentDetailView

urlpatterns = [
    path("payments/", PaymentListView.as_view(), name="payment-list"),  # List & Create payments
    path("payments/<int:payment_id>/", PaymentDetailView.as_view(), name="payment-detail"),  # Retrieve, update, delete
]
