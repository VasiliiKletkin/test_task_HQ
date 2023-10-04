from django.urls import include, path

app_name = 'lessons_api'

urlpatterns = [
    path('lessons/', include('internal_api.lessons_api.urls', namespace="lessons_api")),
    path('products/', include('internal_api.products_api.urls', namespace="products_api")),
]
