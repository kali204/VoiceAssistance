import requests
from feedparser import parse
from jarvis1 import speak
def get_news_from_source(url):
    news_data = parse(url)
    news_list = []

    for entry in news_data.entries:
        news_list.append({
            'title': entry.title,
            'summary': entry.summary
        })

    return news_list

def get_top_headlines():
    news_list = []
    news_sources = [
        'https://news.google.com/rss/search?q=global+warming&hl=en-US&gl=US',
        'https://news.google.com/rss/search?q=tech+news&hl=en-US&gl=US',
        'https://news.google.com/rss/search?q=entertainment+news&hl=en-US&gl=US',
        'https://news.google.com/rss/search?q=sports+news&hl=en-US&gl=US'
    ]

    for source in news_sources:
        news_list.extend(get_news_from_source(source))

    return news_list[:10] # return only top 10 headlines

