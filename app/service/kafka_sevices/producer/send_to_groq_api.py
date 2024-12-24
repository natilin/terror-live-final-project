import os
import time

from dotenv import load_dotenv

from app.service.kafka_sevices.producer.generic_producer import produce
from app.service.news_api_service import get_news
load_dotenv(verbose=True)

def send_news_to_groq_api_producer():
    counter = 0
    while True:
        counter += 1
        news_list = get_news(counter)
        produce(topic=os.environ.get('SEND_NEWS_TO_GROQ_TOPIC'), value=news_list)
        time.sleep(120)