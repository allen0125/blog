from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="article/pages/index.html"), name='index'),
    path('blog', views.PostListView.as_view(), name='blog_list'),
    path('<post_id>/', views.PostDetailView.as_view(), name='blog_detail'),
    path('todolist', views.TodoDetailView.as_view(), name='todolist'),
    path('about', views.AllenCVView.as_view(), name='about'),
]
