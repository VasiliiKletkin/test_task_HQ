from lessons.models import Lesson
from rest_framework.viewsets import ModelViewSet

from .serializers import LessonSerializer


class LessonViewSet(ModelViewSet):
    """
    API endpoint that allows lessons to be viewed or edited.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_superuser:
            return qs.filter(products__in=self.request.user.bought_products.all()).prefetch_related('lessons_info')
        return qs