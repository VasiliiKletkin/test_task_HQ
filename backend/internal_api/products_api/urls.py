from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

app_name = 'products_api'

urlpatterns = [
    path('', include(router.urls)),
]
