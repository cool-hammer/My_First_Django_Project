from django.shortcuts import (
    render, redirect
)
from .models import Article
from .forms import ArticleForm
# Create your views here.


def create(request):
    
    if request.method == 'POST':
        article = Article()
        article_form = ArticleForm(request.POST)
        
        if article_form.is_valid():
            
            cleaned_data = article_form.cleaned_data
            
            article.title = cleaned_data['title']
            article.content = cleaned_data['content']
            
            article.save()
            
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    
    context = {
        'article_form': article_form,
    }
    
    return render(request, 'edit.html', context)

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


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'POST':
        
        article_form = ArticleForm(request.POST)
        
        if article_form.is_valid():
            cleaned_data = article_form.cleaned_data
            
            article.title = cleaned_data['title']
            article.content = cleaned_data['content']
            
            article.save()
            
            return redirect('articles:detail', article_pk)
    else:
        data = {
            'title': article.title,
            'content': article.content,
        }
        article_form = ArticleForm(data=data)
    
    context = {
        'article': article,
        'article_form': article_form,
    }
    
    return render(request, 'edit.html', context)
    


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')