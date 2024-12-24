from datetime import datetime
from toolz import get_in
from app.db.mongo_database import events_collection


def insert_new_terror(terror_news: dict):
    doc = {
        "date":  datetime.strptime(terror_news["date"], "%Y-%m-%d"),
        "location":{
            "city": terror_news["city"],
            "country": terror_news["country"],
            "latitude": get_in(["coordinates", "lat"], terror_news),
            "longitude": get_in(["coordinates", "lng"], terror_news)
        },
        "summary": terror_news["body"]
    }
    events_collection.insert_one()