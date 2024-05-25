from django.test import TestCase
from django.urls import reverse

from .models import Book

class TestBooks(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book1 = Book.objects.create(
            title='title1',
            text="text1",
            author="author1",
            cost=111.111
        )

    def test_book_str(self):
        self.assertEqual(str(self.book1), self.book1.title)

    def test_404_page_if_object_not_found(self):
        response = self.client.get(reverse("book_detail", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_book_view(self):
        self.assertEqual(self.book1.title, "title1")
        self.assertEqual(self.book1.text, "text1")
        self.assertEqual(self.book1.author, "author1")
        self.assertEqual(self.book1.cost, 111.111)

    def test_book_list_url(self):
        response = self.client.get("/books/list/")
        self.assertEqual(response.status_code, 200)

    def test_book_list_name(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)

    def test_book_list_component(self):
        response = self.client.get(reverse("book_list"))
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.text)
        self.assertContains(response, self.book1.author)
        self.assertContains(response, self.book1.cost)

    def test_book_list_template_used(self):
        response = self.client.get(reverse("book_list"))
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_url(self):
        response = self.client.get(f"/books/{self.book1.id}/")
        self.assertEqual(response.status_code, 200)

    def test_book_detail_name(self):
        response = self.client.get(reverse("book_detail", args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_component(self):
        response = self.client.get(reverse("book_detail", args=[self.book1.id]))
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.text)
        self.assertContains(response, self.book1.author)
        self.assertContains(response, self.book1.cost)

    def test_book_detail_template_used(self):
        response = self.client.get(reverse("book_detail", args=[self.book1.id]))
        self.assertTemplateUsed(response, "books/book_detail.html")