from relationship_app.models import Author, Book, Library, Librarian

# 1. Create sample data
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)
library = Library.objects.create(name="Central Library")
library.books.set([book1, book2])
librarian = Librarian.objects.create(name="Alice", library=library)

# 2. Query all books by a specific author
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:", books_by_author)

# 3. List all books in a library
books_in_library = library.books.all()
print("Books in library:", books_in_library)

# 4. Retrieve the librarian for a library
print("Librarian for library:", library.librarian)
