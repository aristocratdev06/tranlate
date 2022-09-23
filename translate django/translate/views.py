from django.shortcuts import render, get_object_or_404
from .models import TranslatePage


def home(request):
    
    return render(request, "home.html")

def translate(request, slug):
    malumot = get_object_or_404(TranslatePage, slug=slug)
    return render(request, "translate.html", {"malumot":malumot})