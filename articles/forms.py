from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['user', 'like_users']
        labels = {
            'title': '제목',
            'content': '내용',
        }


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['user', 'article', 'like_users']
        labels = {
            'content': '내용',
        }

