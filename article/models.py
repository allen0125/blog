from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)  # 博客题目
    is_bio = models.BooleanField(default=False)  # 是否是bio
    is_blog = models.BooleanField(default=True) # 是否为博客文章
    is_todolist = models.BooleanField(default=False)
    category = models.CharField(max_length = 50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = MarkdownxField(default='') # 博客文章正文

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-date_time']

    def get_absolute_url(self):
        abs_url = "/" + str(self.id) + "/"
        return abs_url

    @classmethod
    def get_blog_list(cls):
        queryset = cls.objects.filter(is_blog=True)
        return queryset

    @classmethod
    def get_bio(cls):
        queryset = cls.objects.filter(is_bio=True)[0]
        return queryset

    @classmethod
    def get_todolist(cls):
        queryset = cls.objects.filter(is_todolist=True)[0]
        return queryset
