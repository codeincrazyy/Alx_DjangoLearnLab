from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author (use objects.filter)
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # <- explicit filter
        print(f"Books by {author.name}:")
        for book in books:
            print("-", book.title)
    except Author.DoesNotExist:
        print("Author not found.")


# Query 2: List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name} library:")
        for book in books:
            print("-", book.title)
    except Library.DoesNotExist:
        print("Library not found.")


# Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")


# Example usage
if __name__ == "__main__":
    get_books_by_author("J.K. Rowling")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
