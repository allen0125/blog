from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^blog', views.home, name='home'),
    url(r'^blog', views.PostListView.as_view(), name='blog_list'),
    # url(r'^(\d+)/', views.detail, name='detail'),
    path(r'<post_id>/', views.PostDetailView.as_view(), name='blog_detail'),
    # path('todolist', views.TodoDetailView.as_view(), name='todolist'),
    # path('about', views.AllenCVView.as_view(), name='about'),
]
