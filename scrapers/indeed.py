# scrapers/indeed.py
import requests
from bs4 import BeautifulSoup

def scrape_indeed(keyword):
    results = []
    url = f"https://www.indeed.com/jobs?q={keyword}&limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.select("a.tapItem")

    for job in job_cards:
        title_tag = job.select_one("h2.jobTitle span")
        link = "https://www.indeed.com" + job["href"]
        title = title_tag.text.strip() if title_tag else "No Title"

        results.append({
            "title": title,
            "link": link
        })

    return results
