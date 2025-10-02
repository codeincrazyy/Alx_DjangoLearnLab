from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
import datetime

# ListView: Anyone can view the list of books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# DetailView: Anyone can view a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# CreateView: Only authenticated users can create
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Must be logged in

    def perform_create(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        current_year = datetime.date.today().year
        if publication_year > current_year:
            raise ValidationError({"publication_year": "Cannot set publication year in the future."})
        serializer.save()

# UpdateView: Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Must be logged in

    def perform_update(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        current_year = datetime.date.today().year
        if publication_year > current_year:
            raise ValidationError({"publication_year": "Cannot update book to a future year."})
        serializer.save()

# DeleteView: Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Must be logged in
