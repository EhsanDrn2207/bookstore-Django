from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.BookList.as_view(), name="book_list"),
    path("<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("create/", views.BookCreate.as_view(), name="book_create"),
    path("<int:pk>/update/", views.BookUpdate.as_view(), name="book_update"),
    path("<int:pk>/delete/", views.BookDelete.as_view(), name="book_delete"),
]