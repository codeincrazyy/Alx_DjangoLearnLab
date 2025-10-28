from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book
import datetime

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Create authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="J.R.R. Tolkien")
        # Create books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(title="The Hobbit", publication_year=1937, author=self.author2)
        self.client = APIClient()

    # ---------------------------
    # Test ListView with filtering, search, ordering
    # ---------------------------
    def test_book_list(self):
        # Test without authentication
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Filter by publication_year
        response = self.client.get(reverse("book-list"), {"publication_year": 1937})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

        # Search by title
        response = self.client.get(reverse("book-list"), {"search": "1984"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

        # Ordering by title descending
        response = self.client.get(reverse("book-list"), {"ordering": "-title"})
        self.assertEqual(response.data[0]['title'], "The Hobbit")

    # ---------------------------
    # Test CreateView with authentication
    # ---------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Animal Farm", "publication_year": 1945, "author": self.author1.id}
        response = self.client.post(reverse("book-create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Animal Farm")

    def test_create_book_unauthenticated(self):
        data = {"title": "Animal Farm", "publication_year": 1945, "author": self.author1.id}
        response = self.client.post(reverse("book-create"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # Test UpdateView
    # ---------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {"title": "1984 Revised"}
        response = self.client.patch(reverse("book-update", args=[self.book1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "1984 Revised")

    def test_update_book_unauthenticated(self):
        data = {"title": "1984 Revised"}
        response = self.client.patch(reverse("book-update", args=[self.book1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # Test DeleteView
    # ---------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(reverse("book-delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(reverse("book-delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
