from django.db import models
from django.conf import settings  # ✅ Use settings.AUTH_USER_MODEL to avoid circular import
from datetime import timedelta  # ✅ Import timedelta for default duration

User = settings.AUTH_USER_MODEL  # ✅ Dynamically reference the User model


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)  # ✅ Unique for folder mapping
    display_name = models.CharField(max_length=255, blank=True, null=True)  # ✅ User-friendly name
    description = models.TextField(blank=True, null=True)  # ✅ Added Description Field
    total_videos = models.IntegerField(default=0, editable=False)  # ✅ Auto-updated
    total_duration = models.DurationField(default=timedelta(0), editable=False, null=True, blank=True)  # ✅ Fixed summation issue

    def update_video_stats(self):
        """Automatically update total_videos and total_duration."""
        videos = self.videos.filter(status="Active")
        self.total_videos = videos.count()
        self.total_duration = sum((v.duration for v in videos), timedelta(0))  # ✅ Fixed summation issue
        self.save()

    def __str__(self):
        return self.display_name if self.display_name else self.title


class Video(models.Model):
    ACCESS_CHOICES = [
        ("Free", "Free"),
        ("Restricted", "Restricted"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)  # ✅ Original filename with extension
    display_name = models.CharField(max_length=255, blank=True, null=True)  # ✅ User-friendly name
    description = models.TextField(blank=True, null=True)  # ✅ Keep manually editable descriptions
    duration = models.DurationField(default=timedelta(0))  # ✅ Ensured default duration
    video_url = models.TextField()
    video_order = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")
    access_type = models.CharField(max_length=10, choices=ACCESS_CHOICES, default="Restricted")
    author = models.CharField(max_length=255, default="James")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("course", "video_order")
        ordering = ["video_order"]

    def __str__(self):
        return self.display_name if self.display_name else self.title

    def save(self, *args, **kwargs):
        """Ensure course stats are updated when a video is added/updated."""
        super().save(*args, **kwargs)
        self.course.update_video_stats()

    def delete(self, *args, **kwargs):
        """Ensure course stats are updated when a video is deleted."""
        super().delete(*args, **kwargs)
        self.course.update_video_stats()


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="progress")
    last_watched = models.DateTimeField(auto_now=True)
    watched_duration = models.DurationField(default=timedelta(0))  # ✅ Fixed default duration issue

    class Meta:
        unique_together = ("user", "video")
        indexes = [models.Index(fields=["user", "video"])]

    def __str__(self):
        return f"{self.user} - {self.video.title} ({self.watched_duration})"


class CourseRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="registrations")
    registered_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # ✅ Track if user dropped the course

    class Meta:
        unique_together = ("user", "course")
        indexes = [models.Index(fields=["user", "course"])]

    def __str__(self):
        return f"{self.user} registered for {self.course.title} ({'Active' if self.is_active else 'Dropped'})"
