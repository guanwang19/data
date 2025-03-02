from django.db import models
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    total_videos = models.IntegerField(default=32)
    total_duration = models.DurationField(default="16:00:00")

    def __str__(self):
        return self.title

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    video_url = models.TextField()
    video_order = models.IntegerField()

    class Meta:
        unique_together = ('course', 'video_order')

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    last_watched = models.DateTimeField(auto_now=True)
    watched_duration = models.DurationField(default="00:00:00")

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return f"{self.user.email} - {self.video.title}"


class CourseRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.email} registered for {self.course.title}"
