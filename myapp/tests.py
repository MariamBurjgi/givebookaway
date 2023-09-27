# myapp/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class BookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            # Add other fields as needed
        }
        self.book = Book.objects.create(**self.book_data)

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        response = self.client.post(reverse('book-list'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Assuming there's already one book in the database

    # Add more test methods to cover other API endpoints and scenarios

