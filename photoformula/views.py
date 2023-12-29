from django.shortcuts import render
from .models import Course, Lesson, Instructor, Material
# Create your views here.


def main(request):
    category = Course.objects.filter(category=True)
    return render(request, 'index.html')

