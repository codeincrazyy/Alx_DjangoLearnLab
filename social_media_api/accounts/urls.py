from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, CustomAuthToken, ProfileView,UserViewSet,follow_user, unfollow_user 

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
]
