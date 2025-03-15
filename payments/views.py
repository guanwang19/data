from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment
from cart.models import Cart
from .utils import generate_invoice  # Import invoice generation utility

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items:
        return redirect("cart:cart_detail")

    for item in cart_items:
        Payment.objects.create(
            user=request.user, 
            course=item.course, 
            amount=item.course.price, 
            status="Completed",
            payment_method="Credit Card"  # Default method for now
        )

    cart_items.delete()  # Empty cart after purchase
    return redirect("payments:payment_summary")

@login_required
def payment_summary(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, "payments/payment_summary.html", {"payments": payments})

@login_required
def download_invoice(request, payment_id):
    return generate_invoice(payment_id)

