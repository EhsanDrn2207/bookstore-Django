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

    def test_book_create_url(self):
        response = self.client.get("/books/create/")
        self.assertEqual(response.status_code, 200)

    def test_book_create_name(self):
        response = self.client.get(reverse("book_create"))
        self.assertEqual(response.status_code, 200)

    def test_book_create_form(self):
        response = self.client.post(path=reverse("book_create"), data={
            "title": "title2",
            "text": "text2",
            "author": "author2",
            "cost": 222.222,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().title, "title2")
        self.assertEqual(Book.objects.last().text, "text2")
        self.assertEqual(Book.objects.last().author, "author2")
        self.assertEqual(float(Book.objects.last().cost), 222.222)

    def test_book_create_template_used(self):
        response = self.client.get(reverse("book_create"))
        self.assertTemplateUsed(response, "books/book_create.html")

    def test_book_update_url(self):
        response = self.client.get(f"/books/{self.book1.id}/update/")
        self.assertEqual(response.status_code, 200)

    def test_book_update_name(self):
        response = self.client.get(reverse("book_update", args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_update_view(self):
        response = self.client.post(path=reverse("book_update", args=[self.book1.id]), data={
            "title": "title3",
            "text": "text3",
            "author": "author3",
            "cost": 333.333
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.first().title, "title3")
        self.assertEqual(Book.objects.first().text, "text3")
        self.assertEqual(Book.objects.first().author, "author3")
        self.assertEqual(float(Book.objects.first().cost), 333.333)

    def test_delete_book_url(self):
        response = self.client.get(f"/books/{self.book1.id}/delete/")
        self.assertEqual(response.status_code, 200)

    def test_delete_book_url(self):
        response = self.client.get(reverse("book_delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_book_view(self):
        response = self.client.post(path=reverse("book_delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_book_template_used(self):
        response = self.client.get(reverse("book_delete", args=[self.book1.id]))
        self.assertTemplateUsed(response, "books/book_delete.html")
