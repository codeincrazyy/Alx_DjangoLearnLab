from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# ListView with optional filtering
# -----------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow filtering by title
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']  # Filter by book title or author name

# -----------------------------
# DetailView
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# -----------------------------
# CreateView with authentication and validation
# -----------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create

    def perform_create(self, serializer):
        """
        Optionally, associate the book with the current user or handle extra logic.
        """
        serializer.save()  # Can add extra fields here if needed

# -----------------------------
# UpdateView with authentication and validation
# -----------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can update

    def perform_update(self, serializer):
        """
        Can add custom update logic here (e.g., logging, audit trails).
        """
        serializer.save()

# -----------------------------
# DeleteView with admin permission
# -----------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can delete
