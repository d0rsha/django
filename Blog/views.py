from django import forms
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm, RawArticleForm
from .models import Article


# Create your views here.
def blog_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "blog/article_list.html", context)


def article_detail_view(request, id):
    try:
        obj = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "blog/article_details.html", context)


def article_create_view(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, "blog/article_create.html", context)


def add(request):
    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            form.save()    # saves a new 'Lala' object to the DB
