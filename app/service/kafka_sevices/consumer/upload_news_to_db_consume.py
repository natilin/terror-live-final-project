import json
import os

from dotenv import load_dotenv
from kafka import KafkaConsumer
load_dotenv(verbose=True)

def upload_news_to_db_consume():
    consumer = KafkaConsumer(
        os.environ["UPLOAD_NEWS_TO_DB"],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset="latest",
    )
    print("'UPLOAD_NEWS_TO_DB consumer' is started")
    for message in consumer:
        print(f"Consumer received message : {message.value['title']}")


if __name__ == "__main__":
    upload_news_to_db_consume()