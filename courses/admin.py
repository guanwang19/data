from django.contrib import admin
from courses.models import Course, Video

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "display_name", "description", "total_videos", "total_duration")  # ✅ Include 'description'
    list_editable = ("display_name", "description")  # ✅ Allow inline editing
    search_fields = ("title", "display_name")  # ✅ Enable search
    list_filter = ("total_videos",)  # ✅ Filter by number of videos
    readonly_fields = ("total_videos", "total_duration")  # ✅ Prevent manual changes to auto-generated fields

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "display_name", "description", "course", "status", "video_order", "added_at")  # ✅ Include 'description'
    list_editable = ("display_name", "description")  # ✅ Allow inline editing
    search_fields = ("title", "display_name", "course__title")  # ✅ Enable search by video title & course
    list_filter = ("course", "status", "access_type")  # ✅ Filter by course, status, and access type
    readonly_fields = ("video_url", "added_at")  # ✅ Prevent manual editing of system-generated fields
