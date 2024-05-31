from django.shortcuts import render
from django.views import generic

from .models import Book
from .forms import BookForm
from django.urls import reverse, reverse_lazy


class BookList(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 4


class BookDetail(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class BookCreate(generic.CreateView):
    model = Book
    template_name = "books/book_create.html"
    fields = ["title", "text", "author", "cost", "translator", "publication", "cover"]


class BookUpdate(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_update.html"


class BookDelete(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"

    def get_success_url(self):
        return reverse("book_list")
