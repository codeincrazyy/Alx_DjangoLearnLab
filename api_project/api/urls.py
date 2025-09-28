from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Router for BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),              # CRUD endpoints
    path('api-token-auth/', obtain_auth_token),  # Token retrieval endpoint
]
