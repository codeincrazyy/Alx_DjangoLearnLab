from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer is responsible for converting Book model instances
# into JSON and validating incoming data when creating/updating Books.
#
# Fields: Includes all fields from the Book model.
# Validation:
# - Ensures "publication_year" is not greater than the current year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer is responsible for serializing Author instances.
#
# Fields:
# - id: Author's unique identifier
# - name: The name of the author
# - books: A nested list of BookSerializer objects
#
# Relationship handling:
# Because in the Book model we defined "related_name='books'",
# we can access all books for an author as "author.books".
# This serializer uses BookSerializer (many=True) to display
# all related books inline whenever an Author is serialized.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
