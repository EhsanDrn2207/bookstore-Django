from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args={self.id})
