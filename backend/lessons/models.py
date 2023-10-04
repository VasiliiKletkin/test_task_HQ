from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    video_duration = models.DurationField()
    product = models.ManyToManyField(Product, related_name='lessons')
    
    def __str__(self):
        return self.title


class LessonInfo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessons_info')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons_info')
    watched = models.CharField(max_length=100)
    
    def __str__(self):
        return f"info {self.lesson}"