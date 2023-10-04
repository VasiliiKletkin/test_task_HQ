from django.contrib import admin
from lessons.models import Lesson


class LessonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lesson, LessonAdmin)