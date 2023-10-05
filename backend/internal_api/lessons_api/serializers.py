from lessons.models import Lesson, LessonInfo
from rest_framework import serializers


class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = ['watched', 'lesson', 'user', 'is_watched']

class LessonSerializer(serializers.ModelSerializer):
    lessons_info = LessonInfoSerializer(many=True)
    class Meta:
        model = Lesson
        fields = ['title', 'url', 'video_duration', 'lessons_info']
