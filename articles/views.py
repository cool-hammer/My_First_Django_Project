from django.shortcuts import (
    render, redirect
)
from .models import Article
# Create your views here.

def new(request):
    return render(request, 'new.html')


def create(request):
    article = Article()
    
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article.title = title
    article.content = content
    
    article.save()
    
    return redirect('/articles/new/')