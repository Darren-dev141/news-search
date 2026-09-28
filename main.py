import os
import requests

api = os.environ.get("NEWSAPI_KEY")
if not api:
    raise SystemExit("Set the NEWSAPI_KEY environment variable first (get a free key at https://newsapi.org).")
def lookup(query):
    r = requests.get(f"https://newsapi.org/v2/everything?q={query}&from=2023-08-27&sortBy=popularity&apiKey={api}")
    content = r.json()
    print(type(content))
    articles = content['articles']
    print(type(articles))
    i = 1

    while i < len(articles):
        print(content['articles'][i]['title'] + ", Written By " + content['articles'][i]['author'])
        i += 1

lookup(input("Search term"))

