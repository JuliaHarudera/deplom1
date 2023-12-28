from django.contrib import admin
from .models import Course
from .models import Lesson
from .models import Instructor
from .models import Material


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Material)