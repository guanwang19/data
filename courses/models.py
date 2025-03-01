from django.db import models
from users.models import User  # Import User model

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    total_videos = models.IntegerField(default=32)
    total_duration = models.DurationField(default='16:00:00')

    def __str__(self):
        return self.title

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    video_url = models.URLField()
    video_order = models.IntegerField()

    class Meta:
        unique_together = ('course', 'video_order')

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    last_watched = models.DateTimeField(auto_now=True)
    watched_duration = models.DurationField(default='00:00:00')

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return f"{self.user.email} - {self.video.title} ({self.watched_duration})"

class VideoAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, unique=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.video.title} (Expires: {self.expires_at})"
