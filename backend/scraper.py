import requests
import json
import xml.etree.ElementTree as ET

NEWS_FILE = "news.json"
RSS_URL = "https://www.practicalecommerce.com/feed"

def scrape_practicalecommerce_rss():
    response = requests.get(RSS_URL)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    articles = []
    for item in root.findall(".//item"):
        title = item.findtext("title")
        link = item.findtext("link")
        description = item.findtext("description")
        articles.append({
            "title": title,
            "url": link,
            "summary": description
        })
    with open(NEWS_FILE, "w") as f:
        json.dump(articles, f, indent=2)

if __name__ == "__main__":
    scrape_practicalecommerce_rss() 