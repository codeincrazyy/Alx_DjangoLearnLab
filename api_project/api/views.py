from rest_framework import generics
from .models import Book
from .serializers import BookSerializer  # must match the class name exactly

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
