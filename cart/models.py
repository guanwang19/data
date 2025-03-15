from django.db import models
from django.conf import settings  # ✅ Best Practice for referencing User
from courses.models import Course

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ Dynamic User Reference
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)  # ✅ Use string reference for Course
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.course.title}"  # ✅ Using `email` (more unique than `username`)

