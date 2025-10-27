from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView

# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()
    output = "List of Books:\n\n"
    for book in books:
        output += f"Title: {book.title}, Author: {book.author.name}\n"
    return HttpResponse(output, content_type="text/plain")


# Class-based view to display library details with all books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # optional if using template
    context_object_name = "library"

    def render_to_response(self, context, **response_kwargs):
        library = context['library']
        books = library.books.all()
        output = f"Library: {library.name}\nBooks:\n"
        for book in books:
            output += f"- {book.title} by {book.author.name}\n"
        return HttpResponse(output, content_type="text/plain")