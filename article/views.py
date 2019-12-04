# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Article


# Create your views here.
def index(request):
    template = loader.get_template('article/pages/index.html')
    return HttpResponse(template.render({}, request))


class PostListView(ListView):
    queryset = Article.get_blog_list()
    context_object_name = "post_list"
    template_name = "article/pages/blog.html"


class PostDetailView(DetailView):
    queryset = Article.get_blog_list()
    template_name = 'article/pages/post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class TodoDetailView(ListView):
    queryset = Article.objects.filter(title="要填的坑")[0]
    template_name = 'article/pages/post.html'
    context_object_name = 'post'


class AllenCVView(ListView):
    queryset = Article.get_bio()
    template_name = 'article/pages/post.html'
    context_object_name = 'post'
