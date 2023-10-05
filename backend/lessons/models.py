from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    video_duration = models.DurationField(default=0)
    products = models.ManyToManyField(Product, related_name='lessons', blank=True)
    
    def __str__(self):
        return self.title


class LessonInfo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessons_info')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons_info')
    watched = models.DurationField(default=0)
    @property
    def is_watched(self):
        try:
            return True if self.watched / self.lesson.video_duration * 100 > 80 else False
        except Exception:
            return False

    def __str__(self):
        return f"info {self.lesson}"