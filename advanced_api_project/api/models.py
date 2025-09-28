from django.db import models

# -----------------------------
# Author Model
# -----------------------------
class Author(models.Model):
    """
    Represents an author in the system.
    
    Fields:
    - name: The full name of the author (string, max 100 characters).
    
    Relationships:
    - One-to-Many with Book: An author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        # Human-readable representation of the author
        return self.name

# -----------------------------
# Book Model
# -----------------------------
class Book(models.Model):
    """
    Represents a book in the system.
    
    Fields:
    - title: The title of the book (string, max 200 characters).
    - publication_year: The year the book was published (integer).
    - author: ForeignKey linking to Author model (One-to-Many relationship).
    
    Relationships:
    - Many books can belong to one author.
    - Deleting an author will delete all their books (CASCADE).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,  # Delete books if author is deleted
        related_name='books'       # Allows access via author.books.all()
    )

    def __str__(self):
        # Human-readable representation of the book
        return self.title
