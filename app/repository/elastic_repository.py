from datetime import datetime

from app.db.elastic_database import get_elasticsearch_client


def insert_new_terror_elastic(terror_news: dict):
    doc = {
            "summary": terror_news["body"],
            "date": datetime.strptime(terror_news["date"], "%Y-%m-%d")
        }
    es = get_elasticsearch_client()
    es.index(index="new_terror_event", body=doc)


