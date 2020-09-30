from django.shortcuts import (
    render, redirect
)
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods

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
    comments = Comment.objects.filter(article=article)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
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


@require_POST
@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()

        return redirect('articles:detail', article_pk)

    context = {
        'comment_form': comment_form,
        'article': article,
    }

    return render(request, 'detail.html', context)
