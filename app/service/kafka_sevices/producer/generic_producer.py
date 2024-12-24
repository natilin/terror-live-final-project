import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer


load_dotenv(verbose=True)

def produce(topic: str, value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode()
    )
    producer.send(
        topic=topic,
        value=value
    )
    producer.flush()
