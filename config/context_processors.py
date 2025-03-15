# config/context_processors.py
from django.apps import apps

def global_context(request):
    Course = apps.get_model('courses', 'Course')
    return {"courses": Course.objects.all()}
