from lessons.models import Lesson
from rest_framework.viewsets import ModelViewSet

from .serializers import LessonSerializer


class LessonViewSet(ModelViewSet):
    """
    API endpoint that allows lessons to be viewed or edited.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer