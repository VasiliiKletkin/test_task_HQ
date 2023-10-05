from django.contrib import admin
from lessons.models import Lesson, LessonInfo


class LessonAdmin(admin.ModelAdmin):
    pass
class LessonInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonInfo, LessonInfoAdmin)