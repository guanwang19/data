from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()  # ✅ Dynamically get User model to avoid circular imports

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Completed", "Completed"), ("Failed", "Failed")],
        default="Pending",
    )
    payment_method = models.CharField(max_length=50, choices=[("Credit Card", "Credit Card"), ("PayPal", "PayPal")])
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} by {self.user.username} - {self.status}"


