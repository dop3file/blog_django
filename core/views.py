from django.shortcuts import render, redirect
from core.models import Article, Comment
from django.core.paginator import Paginator
import core.utils as utils


def index(request):
    context = {}
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)

    page_number = request.GET.get('page', 1)
    context['articles'] = paginator.get_page(page_number)

    return render(request, 'index.html', context=context)


def get_article(request, id):
    try:
        if request.method == "GET":
            context = {}
            article = Article.objects.get(id=id)
            context['article'] = article
            comments = Comment.objects.filter(article=article).all()
            context['comments'] = reversed(comments)
            return render(request, 'article.html', context=context)
        elif request.method == "POST":
            context = {}

            comment = request.POST.get('comment')
            comment = Comment(text=comment, article=Article.objects.get(id=id))
            comment.save()
            
            article = Article.objects.get(id=id)
            context['article'] = article
            comments = Comment.objects.filter(article=article).all()
            context['comments'] = reversed(comments)
            request.method = "GET"
            return render(request, 'article.html', context=context) 
            
    except Article.DoesNotExist:
        context = {}
        context['error'] = 'Такой записи не существует'
        return render(request, 'article.html', context=context)


def get_all_articles(request):
    context = {}
    context['articles'] = Article.objects.all()
    return render(request, 'all_articles.html', context=context)


def search_article(request):
    context = {}
    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        context['articles'] = utils.search(Article, search_text)
        context['search_text'] = search_text
    return render(request, 'search.html', context=context)