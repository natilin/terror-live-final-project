import json

from dotenv import load_dotenv
from groq import Groq
load_dotenv(verbose=True)

def get_event_details(news: str) -> dict:
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "        I will give you a description of news, and you tell me which category it belongs to:  general news, current terrorist event, or historical terrorist event. Additionally, if it is a historical or current terrorist event, provide a location in the format of city and country, and return the result in JSON format in the json will be 3 keys: category, country and city  . \n"
            },
            {
                "role": "user",
                "content" : news
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    res = completion.choices[0].message.content

    return json.loads(res)

