from rest_framework import serializers
from .models import Book, Author
from datetime import date

# -----------------------------
# BookSerializer
# -----------------------------
class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model.
    
    Fields included: All fields of the Book model (title, publication_year, author).
    
    Custom validation:
    - Ensures publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Validate that the publication year is not greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# -----------------------------
# AuthorSerializer
# -----------------------------
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model.
    
    Fields included:
    - name: Author's name
    - books: Nested list of books authored by this author
    
    Relationship handling:
    - The 'books' field uses the related_name defined in the Book model.
    - It dynamically serializes all books related to an author using BookSerializer.
    - 'read_only=True' ensures books are displayed but cannot be created via AuthorSerializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
