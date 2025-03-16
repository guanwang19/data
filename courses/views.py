from django.shortcuts import render, get_object_or_404
from .models import Course, Video

def course_list(request):
    """Fetches all available courses and sends them to the template"""
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})

def course_detail(request, course_id):
    """Fetches a specific course and its videos"""
    course = get_object_or_404(Course, pk=course_id)

    # Ensure video URLs are correctly formatted
    videos = []
    for video in course.videos.all():
        duration_minutes = round(video.duration.total_seconds() / 60) if video.duration else 0
        videos.append({
            "display_name": video.display_name or video.title,
            "duration": duration_minutes,
            "description": video.description or "No description available.",
            "video_url": f"/videos/{video.video_url}"  # ✅ Ensure correct URL path
        })

    return render(request, "courses/course_detail.html", {"course": course, "videos": videos})



