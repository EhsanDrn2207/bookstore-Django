from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import CustomUserModel


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


class SignUpFormTest(TestCase):
    def test_signup_url(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_template_used(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "registration/signup_page.html")

    def test_signup_form(self):
        username = "new_username"
        email = "new_email"
        user = get_user_model().objects.create_user(
            username=username,
            email=email
        )
        # get_user_model ---> CustomUserModel

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "new_username")
        self.assertEqual(get_user_model().objects.all()[0].email, "new_email")
