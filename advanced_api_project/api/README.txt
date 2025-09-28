# Book API Views Documentation

## Endpoints and Permissions

| Endpoint                        | Method | View               | Permission           | Description |
|---------------------------------|--------|------------------|-------------------|-------------|
| /api/books/                      | GET    | BookListView       | AllowAny           | Retrieve a list of all books. Supports search by title and author. |
| /api/books/<id>/                 | GET    | BookDetailView     | AllowAny           | Retrieve a single book by ID. |
| /api/books/create/               | POST   | BookCreateView     | IsAuthenticated    | Add a new book. Validates publication_year. |
| /api/books/<id>/update/          | PUT    | BookUpdateView     | IsAuthenticated    | Update an existing book by ID. |
| /api/books/<id>/delete/          | DELETE | BookDeleteView     | IsAdminUser        | Delete a book by ID. Admin only. |

## Custom Hooks and Settings

- **perform_create()** in `BookCreateView` can be used to attach extra logic when a book is created (e.g., associating a user or logging activity).  
- **perform_update()** in `BookUpdateView` allows custom logic during updates.  
- **Filtering**: `BookListView` supports filtering books by `title` or `author__name` using the `search` query parameter:  
  Example: `/api/books/?search=Harry`  
- **Validation**: `publication_year` cannot be in the future. This validation is handled in `BookSerializer`.

## Usage Notes

- List and Detail views are open to all users (read-only).  
- Create and Update views require login.  
- Delete view requires admin privileges.  
- Use token-based authentication for secured endpoints.
