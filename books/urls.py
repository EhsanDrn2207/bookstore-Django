from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.BookList.as_view(), name="book_list"),
    path("<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
]