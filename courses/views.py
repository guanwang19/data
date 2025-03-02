from rest_framework import generics
from .models import Course, Video, UserProgress
from .serializers import CourseSerializer, VideoSerializer, UserProgressSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Course Platform! from courses/views.py")

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class UserProgressView(generics.RetrieveAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
