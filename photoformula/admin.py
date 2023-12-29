from django.contrib import admin
from .models import Course, Lesson, Instructor, Material
from django.utils.safestring import mark_safe


admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Material)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price', 'photo_src_tag')
    list_editable = ('category', 'name', 'price',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Course photo'









