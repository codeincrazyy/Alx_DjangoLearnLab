from django.shortcuts import render
from .models import Library, Book
from django.views.generic import DetailView

# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


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