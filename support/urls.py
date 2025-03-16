from django.urls import path
from .views import contact_view, contact_success_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]