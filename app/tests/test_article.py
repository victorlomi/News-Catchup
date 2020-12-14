import unittest

from app.models import article

class TestArticle(unittest.TestCase):
    """Tests for the class Article."""

    def setUp(self):
        """Set up article and its components"""
        self.source =  {
            "id": "cnn",
            "name": "CNN"
        }
        self.author = "Analysis by Zachary B. Wolf, CNN"
        self.title =  "paying the price of Covid"
        self.description =  "description"
        self.url =  "link1"
        self.urlToImage =  "link2"
        self.publishedAt =  "2020-12-02T05:04:40Z"
        self.content =  "content"
        self.article = article.Article(self.source, self.author, self.title,
            self.description, self.url, self.urlToImage, self.publishedAt, self.content)

    def test_simplify_date(self):
        """Test that date is simplified to year-month-day."""
        self.assertEqual(article.simplify_date(), "2020-12-02")
