from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
import datetime

# -------------------------------
# ListView: Anyone can view the list of books
# Supports filtering, search, and ordering
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    API endpoint that allows books to be viewed with filtering, searching, and ordering.

    Features:
    - Filtering: Users can filter by publication_year and author ID.
    - Searching: Users can search by book title or author name (partial match).
    - Ordering: Users can sort results by title, publication_year, or author name.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields available for exact filtering
    filterset_fields = ['publication_year', 'author']

    # Fields available for text search
    search_fields = ['title', 'author__name']

    # Fields users can order by
    ordering_fields = ['title', 'publication_year', 'author__name']

    # Default ordering
    ordering = ['title']

# -------------------------------
# DetailView: Anyone can view a single book
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# -------------------------------
# CreateView: Only authenticated users can create
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        current_year = datetime.date.today().year
        if publication_year > current_year:
            raise ValidationError({"publication_year": "Cannot set publication year in the future."})
        serializer.save()

# -------------------------------
# UpdateView: Only authenticated users can update
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        current_year = datetime.date.today().year
        if publication_year > current_year:
            raise ValidationError({"publication_year": "Cannot update book to a future year."})
        serializer.save()

# -------------------------------
# DeleteView: Only authenticated users can delete
# -------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
