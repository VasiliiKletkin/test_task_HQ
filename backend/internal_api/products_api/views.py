from products.models import Product
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer