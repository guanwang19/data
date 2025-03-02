from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from django.shortcuts import get_object_or_404

class PaymentListView(APIView):
    """
    Retrieve all payments or create a new payment.
    """
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentDetailView(APIView):
    """
    Retrieve, update, or delete a single payment.
    """
    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, pk=payment_id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, payment_id):
        payment = get_object_or_404(Payment, pk=payment_id)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, payment_id):
        payment = get_object_or_404(Payment, pk=payment_id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
