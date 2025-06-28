# scrapers/remoteok.py
import requests
from bs4 import BeautifulSoup

def scrape_remoteok(keyword):
    results = []
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.select("tr.job")  # 테이블 형식의 리스트

    for job in jobs:
        title_elem = job.select_one("td.position h2")
        link_elem = job.get("data-href")

        if title_elem and link_elem:
            title = title_elem.text.strip()
            link = f"https://remoteok.com{link_elem}"
            results.append({
                "title": title,
                "link": link
            })

    return results
