from django.shortcuts import render
from .models import NewsArticle
from django.shortcuts import render, get_object_or_404

def news_list(request):
    fetch_and_save_news()
    articles = NewsArticle.objects.all()
    
    return render(request, 'news_list.html', {'articles': articles})

def news_detail(request, pk):
    article = NewsArticle.objects.all().order_by('-created_at')
    return render(request, 'news/news_detail.html', {'article': article})

# fetch_news.py

# fetch_news.py

def fetch_and_save_news():
    import requests
    from bs4 import BeautifulSoup
    from django.core.management.base import BaseCommand
    from news.models import NewsArticle
    from newsapi import NewsApiClient

    newsapi = NewsApiClient(api_key='a2be58f9a9df461f9c925b2190082dfe')

    # Fetch top headlines from India
    news_data = newsapi.get_top_headlines(country='in', language='en', page_size=10)

    # Save fetched data to the database, checking for duplicates
    for article in news_data['articles']:
        # Check if the article already exists in the database by source_url
        if not NewsArticle.objects.filter(source_url=article['url']).exists():
            NewsArticle.objects.create(
                title=article['title'],
                content=article['description'],
                source_url=article['url'],
                # Check for 'category' key in the response before using it
                category=article.get('category', 'Uncategorized'),
                img_url=article['urlToImage'],
            )

    print('Successfully fetched and saved news data (avoiding duplicates).')

