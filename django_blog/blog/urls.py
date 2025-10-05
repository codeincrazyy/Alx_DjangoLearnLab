from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    SignupView, home, posts, profile, search_posts,
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, CommentCreateView,
    CommentDeleteView, CommentUpdateView, posts_by_tag
)

urlpatterns = [
    # Authentication
    path('register/', SignupView, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),

    # Blog Posts
    path('', home, name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Search & Tags
    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
]
