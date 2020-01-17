from Blog.views import (add, article_create_view, article_detail_view,
                        blog_list_view)
from django.contrib import admin
from django.urls import path

app_name = 'Blog'
urlpatterns = [
    path('', blog_list_view, name="blog"),
    path('<int:id>/', article_detail_view, name="article-details"),
    path('<int:id>/delete', article_detail_view, name="article-delete"),
    path('create/', article_create_view),
]
