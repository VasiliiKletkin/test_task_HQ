from lessons.models import Lesson, LessonInfo
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = '__all__'
