from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Payment

def generate_invoice(payment_id):
    payment = Payment.objects.get(id=payment_id)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoice_{payment_id}.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 750, f"Invoice for Payment {payment.id}")
    p.drawString(100, 730, f"User: {payment.user.username}")
    p.drawString(100, 710, f"Course: {payment.course.title}")
    p.drawString(100, 690, f"Amount: ${payment.amount}")
    p.drawString(100, 670, f"Status: {payment.status}")
    p.showPage()
    p.save()

    return response
