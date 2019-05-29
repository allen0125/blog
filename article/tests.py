from django.test import TestCase
from .models import Article
# Create your tests here.


class ArticleTestStr(TestCase):

    def setUp(self):
        Article.objects.create(title="Test",
                               category="Test",
                               conten="Content Test")

    def test_article_str(self):
        article_test = Article.objects.get(title="Test")
        self.assertEqual(article_test.__str__(), "Test")
