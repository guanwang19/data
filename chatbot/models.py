
from django.db import models
from users.models import User

class ChatbotQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    query_text = models.TextField()
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query from {self.user.email if self.user else 'Guest'} at {self.created_at}"

