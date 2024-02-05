import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from news.models import NewsArticle
from newsapi import NewsApiClient

class Command(BaseCommand):
    help = 'Fetch latest news and save to the database'

    def handle(self, *args, **options):
        newsapi = NewsApiClient(api_key='a2be58f9a9df461f9c925b2190082dfe')

        # Fetch top headlines from India
        news_data = newsapi.get_top_headlines(country='in', language='en', page_size=10)

        # Print the entire 'article' dictionary to inspect its structure
        for article in news_data['articles']:
            print(article)

            # Save fetched data to the database
            NewsArticle.objects.create(
                title=article['title'],
                content=article['description'],
                source_url=article['url'],
                # Check for 'category' key in the response before using it
                category=article.get('category', 'Uncategorized'),
                img_url=article['urlToImage'],
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved news data.'))
