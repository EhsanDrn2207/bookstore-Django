from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_name(self):
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse("home_page"))
        self.assertTemplateUsed(response, "home_page.html")

    def test_home_page_components(self):
        response = self.client.get(reverse("home_page"))
        self.assertContains(response, "Home Page")
