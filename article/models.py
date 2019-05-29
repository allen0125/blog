from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)  # 博客题目
    is_bio = models.CharField(max_length = 10, null=True)  # 是否是bio
    category = models.CharField(max_length = 50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = MarkdownxField(default='') # 博客文章正文

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-date_time']
