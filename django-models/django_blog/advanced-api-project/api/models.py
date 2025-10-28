from django.db import models

# The Author model represents a book author in the system.
# Each Author has a single "name" field.
# One Author can be linked to multiple Books (One-to-Many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        # Returning the author's name for easy identification in the admin panel
        return self.name


# The Book model represents an individual book.
# Fields:
# - title: name of the book
# - publication_year: year the book was published
# - author: a ForeignKey relationship linking each book to a single Author
#
# Relationship:
# Each Book belongs to one Author.
# The "related_name='books'" allows us to access an Author's books using author.books.all()
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        # Returning book title and publication year for clarity
        return f"{self.title} ({self.publication_year})"
