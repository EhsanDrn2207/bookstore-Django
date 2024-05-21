from django.shortcuts import render
from django.views import generic

from .models import CustomUserModel
from .forms import CustomUserCreationForm


class HomePageView(generic.TemplateView):
    template_name = "home_page.html"


