from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from courses.models import Course

@login_required
def add_to_cart(request, course_id):
    course = Course.objects.get(id=course_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, course=course)
    
    if not created:
        cart_item.quantity += 1  # Optional for multiple licenses
        cart_item.save()
    
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.course.price for item in cart_items)
    return render(request, "cart/cart.html", {"cart_items": cart_items, "total_price": total_price})

@login_required
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart:cart_detail')
