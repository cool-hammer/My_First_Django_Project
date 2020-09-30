from django.shortcuts import (
    render, redirect
)
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')

    if request.method == 'POST':
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
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


@login_required
def update(request, article_pk):

    article = Article.objects.get(pk=article_pk)

    if article.user != request.user:
        return redirect('articles:detail', article_pk)
    
    if request.method == 'POST':

        article_form = ArticleForm(request.POST, instance=article)

        if article_form.is_valid():
            article_form.save()

            return redirect('articles:detail', article_pk)
    else:
        article_form = ArticleForm(instance=article)

    context = {
        'article': article,
        'article_form': article_form,
    }

    return render(request, 'edit.html', context)


def delete(request, article_pk):
    
    article = Article.objects.get(pk=article_pk)
    
    if article.user != request.user:
        return redirect('articles:detail', article_pk)
    
    article.delete()
    return redirect('articles:index')
