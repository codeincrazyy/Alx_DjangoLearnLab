from django.urls import path
from .views import book_list
from .views import list_books
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # function-based view using template
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # class-based view
]
