from django.shortcuts import render

from .models import Author, Article, Comment



def index(request):
    return render(request, 'index.html')
