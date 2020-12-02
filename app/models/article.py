class Article():
    """Stores details about article from the newsapi."""

    def __init__(self, source, author, title, description, url, urlToImage, publishedAt, content):
        """Store source, author, title, description, url, urlToImage, publishedAt, and content."""
        self.source = source 
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
