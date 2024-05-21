from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home_page"),
    path("signup/", views.SingUpPageView.as_view(), name="signup"),
]
