from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog', views.home, name='home'),
    url(r'^(\d+)/', views.detail, name='detail'),
    url(r'^todolist', views.todolist, name='todolist'),
    url(r'^about/', views.allen_about, name='about'),
]
