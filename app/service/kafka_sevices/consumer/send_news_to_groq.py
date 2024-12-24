import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from toolz import get_in

from app.service.api.groq_api_service import get_event_details
from app.service.api.location_api_service import get_coordinates_by_location
from app.service.kafka_sevices.producer.upload_terror_in_db_producer import upload_terror_in_db

load_dotenv(verbose=True)

def send_news_to_groq_consumer():
    consumer = KafkaConsumer(
        os.environ["SEND_NEWS_TO_GROQ_TOPIC"],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset="latest",
    )
    print("'send news to groq consumer' started")
    for message in consumer:
        print(f"Consumer received message : ")
        handle_news(message.value)



def handle_news(news):
    news_list = get_in(["article","results"], news)
    if news_list is None:
        return

    try:
        for new in news_list:
            res = get_event_details(new["body"])
            if res.get("category") in ["current terrorist event", "historical terrorist event"]:
                new["country"] = res["country"]
                new["city"] = res["city"]
                new["coordinates"] = get_coordinates_by_location(res["city"], res["country"])
                upload_terror_in_db(res)

    except Exception:
        return None

if __name__ == "__main__":
    send_news_to_groq_consumer()