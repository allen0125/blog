"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import include, url
from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from article.models import Article

info_dict = {
    'queryset': Article.objects.all(),
    'date_field': 'date_time',
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('sitemap.xml', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
