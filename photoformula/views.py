from django.shortcuts import render
from .models import Course, Lesson, Instructor, Material
# Create your views here.


def main(request):
    category_courses = Course.objects.filter(category=True)
    context = {'category_courses': category_courses, }
    return render(request, 'index.html', context)

