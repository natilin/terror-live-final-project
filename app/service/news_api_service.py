import os

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)
def get_news(page_num):
    api_key = os.environ.get('NEWS_API_KEY')
    body = {
        "action": "getArticles",
        "keyword": "terror attack",
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": page_num,
        "articlesCount": 100,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": [
            "news",
            "pr"
        ],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": api_key
    }
    response = requests.post("https://eventregistry.org/api/v1/article/getArticles", json=body)
    return response.json()


d = get_news(1)

s = 0


