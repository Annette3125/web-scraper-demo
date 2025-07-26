import csv
import json
import certifi
import time
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

robots_parser = RobotFileParser()
robots_txt = requests.get(
    "https://edition.cnn.com/robots.txt", timeout=5, verify=certifi.where()
).text
robots_parser.parse(robots_txt.splitlines())

base_url = "https://edition.cnn.com/"
source = urlparse(base_url).netloc
headlines = []
visited = set()
max_pages = 5
page_count = 0

listing_url = base_url
while True:
    if listing_url in visited:
        print("Already visited", listing_url, " - stopping to avoid a loop.")
        break

    if page_count >= max_pages:
        print(f"Reached max_pages={max_pages} - stopping")
        break

    visited.add(listing_url)
    page_count += 1

    response = requests.get(listing_url, timeout=5, verify=certifi.where())
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    blocks = soup.find_all(class_="container__headline-text")

    for block in blocks:
        text = block.get_text(strip=True)
        link = block.find_parent("a")
        print(f"Heading: {text}")
        if not text or not link:
            continue

        article_url = urljoin(base_url, link["href"])

        if robots_parser.can_fetch("*", article_url):


            article_response = requests.get(
                article_url, timeout=5, verify=certifi.where()
            )
            article_response.raise_for_status()
        else:
            print(f"Disallowed by robots.txt, skipping: {article_url}")
            continue

        article_soup = BeautifulSoup(article_response.text, "html.parser")
        author_tag = article_soup.select_one("span.byline__name")
        author = author_tag.text.strip() if author_tag else None

        date_tag = article_soup.select_one("div.timestamp__published")
        date_date = date_tag.text.strip() if date_tag else None

        if not text or not link or not link.get("href"):
            continue

        headlines.append(
            {
                "source": source,
                "url": article_url,
                "heading": text,
                "date": date_date,
                "author": author,
            }
        )

        print(f"Scraped: {text} — by {author} on {date_date}")
        time.sleep(0.5)

    next_page = soup.find("a", {"aria-label": "Next"})
    if next_page and next_page.get("href"):
        listing_url = urljoin(base_url, next_page["href"])
        time.sleep(1)
    else:
        break


with open("data/headlines1.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, ensure_ascii=False, indent=4)
print(f"Saved {len(headlines)} headlines to headlines1.json")


with open("data/headlines1.csv", "w", encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Source", "url", "Heading", "author", "date"])

    for item in headlines:
        csv_writer.writerow(
            [
                item["source"],
                item["url"],
                item["heading"],
                item["author"] or "",
                item["date"] or "",
            ]
        )
print(f"Saved {len(headlines)} headlines to headlines1.csv")
