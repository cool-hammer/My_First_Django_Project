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
    
    return redirect('/articles/')

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles
    }
    
    return render(request, 'index.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    context = {
        'article': article,
    }
    
    return render(request, 'detail.html', context)