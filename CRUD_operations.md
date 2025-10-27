# CRUD Operations for Book Model

## 1. Create

```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>
# Retrieve the Book instance
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)

# Update the title of the Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

# Delete the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []>

```
