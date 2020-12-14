import unittest

from ..app.models import source

class TestSource(unittest.TestCase):
    """Tests for the class Source."""

    def setUp(self):
        """Set up source and its components"""
        self.source = source.Source('bbc-news', 'BBC News', "images/bbc.jpg")

    def test_create_source(self):
        """Test that sources can be created."""
        self.assertEqual(self.source.id, "bbc-news")
        self.assertEqual(self.source.name, "BBC News")
        self.assertEqual(self.source.image, "images/bbc.jpg")
