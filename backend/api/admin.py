from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from .models import Teacher, Course, CourseStudent, Lesson, VideoMaterial,\
    TextMaterial, Categories


admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(VideoMaterial)
admin.site.register(TextMaterial)
admin.site.register(Categories)


@admin.register(CourseStudent)
class StudentsAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "course" )
    list_filter = ("course", )
    ordering = ("last_name",)
