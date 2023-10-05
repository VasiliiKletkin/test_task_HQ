from django.contrib.auth import get_user_model
from django.db.models import Count, Sum
from lessons.models import LessonInfo
from products.models import Product
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..lessons_api.serializers import LessonSerializer
from .serializers import ProductSerializer

User = get_user_model()


class ProductViewSet(ModelViewSet):
    """
    ProductViewSet provides API endpoints for Products. 

    It has a queryset for all Products and uses the ProductSerializer.

    get_queryset filters Products if user is not a superuser. 

    The lessons() method gets lessons for a Product and returns them serialized.

    The info() method aggregates data on lessons and products and returns it.

    Args:
    self

    Returns:
    Response: DRF response object.

    Raises:
    None
"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_superuser:
            return qs.filter(users=self.request.user)
        return qs

    @action(detail=True, methods=['get'])
    def lessons(self, request, pk):
        product = self.get_object()
        lessons = product.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def info(self, request):
        total_during_time = LessonInfo.objects.aggregate(Sum('watched'))[
            'watched__sum']
        count_users_for_product = Product.objects.values(
            "title").annotate(count_users=Count('users'))
        percent_users_for_product = Product.objects.values(
            "title").annotate(percent=Count('users')/User.objects.count())

        data = {
            "total_during_time": total_during_time,
            "count_users_for_product": count_users_for_product,
            "percent_users_for_product": percent_users_for_product,
        }
        return Response(data)
