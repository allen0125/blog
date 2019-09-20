# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import Http404
from .models import Article
from django.template import loader


# Create your views here.
def index(request):
    try:
        template = loader.get_template('article/pages/index.html')
    except Article.DoesNotExist as e:
        raise Http404('article/pages/404.html')
    return HttpResponse(template.render({}, request))


def home(request):
    try:
        post_list = Article.objects.filter(is_bio='N')  # 获取全部的Article对象

        template = loader.get_template('article/pages/blog.html')

        context = {
            'post_list': post_list,
        }
    except Article.DoesNotExist as e:
        raise Http404('article/pages/404.html')
    return HttpResponse(template.render(context, request))


def detail(request, blog_id):
    try:
        post = Article.objects.get(id=str(blog_id))
        content = {'post': post}
        template = loader.get_template('article/pages/post.html')
    except Article.DoesNotExist as e:
        raise Http404('article/pages/404.html')
    return HttpResponse(template.render(content, request))


def todolist(request):
    try:
        post_list = Article.objects.get(title="要填的坑")
        template = loader.get_template('article/pages/todolist.html')
        context = {
            'post_list': post_list,
        }
    except Article.DoesNotExist as e:
        raise Http404('article/pages/404.html')
    return HttpResponse(template.render(context, request))


def allen_about(request):
    try:
        post = Article.objects.get(title="About")
        content = {'post': post}
        template = loader.get_template('article/pages/post.html')
    except Article.DoesNotExist as e:
        raise Http404('article/pages/404.html')
    return HttpResponse(template.render(content, request))
