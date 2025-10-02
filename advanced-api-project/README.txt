Book API Endpoints
Endpoint	   Method	  Purpose	  Permissions	    Notes / Custom Behavior
/api/books/	    GET	    List all books	Read-only (anyone)	Returns all books serialized with BookSerializer
/api/books/<int:pk>/GET	  Retrieve a single book	Read-only (anyone)	Returns a single book by ID
/api/books/create/	POST  Create a new book	Authenticated users only	Validates publication_year is not in the future before saving
/api/books/<int:pk>/update/	PUT / PATCH	Update an existing book	Authenticated users only	perform_update validates publication_year before saving
/api/books/<int:pk>/delete/	DELETE	Delete a book	Authenticated users only	Simple destroy operation
Custom Hooks / Settings

perform_create and perform_update: Custom methods in DRF generic views that allow server-side logic before saving the model instance.

Permissions:

AllowAny for read-only views (list/detail)

IsAuthenticated for write operations (create/update/delete)

Validation: Ensures no book can have a publication year in the future.