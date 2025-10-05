from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Blog post CRUD URLs (updated to singular 'post')
    path('posts/', views.PostListView.as_view(), name='posts'),                   # List all posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),       # Create new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),# Delete post
]
