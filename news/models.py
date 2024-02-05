from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    category = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    source_url = models.URLField()
    img_url = models.URLField()  # Make sure this field is present

    def __str__(self):
        return self.title
