from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import book_list
from .views import list_books
urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # class-based view

    # User authentication URLs
    path('register/', views.register, name='register'),  # function-based view for registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
