from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    return render(request, 'shop/index.html')


def articles(request):
    articles = Article.objects.order_by('-created_at')
    context = {
        'title': 'Статьи',
        'articles': articles
    }
    return render(request, 'shop/articles.html', context)

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'

    form = ArticleForm()
    context = {
        'form': form,
        'error': error,
        'title': 'Создать статью',     
    }
    return render(request, 'shop/create.html', context)