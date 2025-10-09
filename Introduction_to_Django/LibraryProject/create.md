# Create Operation

````python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>


---

### 2. `retrieve.md`
```markdown
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the Book instance
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)


---

### 3. `update.md`
```markdown
# Update Operation

```python
from bookshelf.models import Book

# Update the title of the Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>


---

### 4. `delete.md`
```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Delete the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []>


---

### 5. `CRUD_operations.md`
You can combine all the above sections into **one file** if required by your assignment. Just copy all four Markdown sections into a single file.

---

#### Steps to create these files on your machine:

**Option 1: Terminal**
```bash
cd ~/desktop/Alx_DjangoLearnLab/Introduction_to_Django
nano create.md  # Paste content, save with CTRL+O, exit with CTRL+X
nano retrieve.md  # Paste content
nano update.md
nano delete.md
nano CRUD_operations.md  # Optional combined file
````
