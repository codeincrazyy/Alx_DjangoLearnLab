from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# ListView: Retrieve all books
# -----------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Returns a list of all books in the system.
    - Anyone can access (read-only).
    - Supports filtering by 'title' or 'author name' using query parameter 'search'.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']
    permission_classes = [permissions.AllowAny]  # No authentication required

# -----------------------------
# DetailView: Retrieve a single book
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/

    Returns details of a single book by its ID.
    - Anyone can access (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# -----------------------------
# CreateView: Add a new book
# -----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/

    Allows authenticated users to create a new book.
    - Permission: IsAuthenticated
    - Validation: Ensures 'publication_year' is not in the future via BookSerializer.
    - Custom hook: perform_create() can be used to attach extra logic if needed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # You can add extra logic here (e.g., logging)
        serializer.save()

# -----------------------------
# UpdateView: Modify an existing book
# -----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<id>/update/

    Allows authenticated users to update an existing book.
    - Permission: IsAuthenticated
    - Validation: Handled by BookSerializer
    - Custom hook: perform_update() allows extending update behavior.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()  # Custom logic can be added here

# -----------------------------
# DeleteView: Remove a book
# -----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/

    Allows only admin users to delete a book.
    - Permission: IsAdminUser
    - Returns HTTP 204 No Content on success.
    """
    queryset = Book.objects.all()
    serializer_class = BookSe_
