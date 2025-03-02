from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'user', 'payment_status', 'payment_amount', 'payment_method', 'transaction_id', 'created_at']
