from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "courses/course_detail.html", {"course": course})

