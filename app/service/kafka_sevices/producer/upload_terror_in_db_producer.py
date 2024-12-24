import os

from dotenv import load_dotenv

from app.service.kafka_sevices.producer.generic_producer import produce
load_dotenv(verbose=True)

def upload_terror_in_db(news: dict):
    produce(os.environ.get('UPLOAD_NEWS_TO_DB'), news)