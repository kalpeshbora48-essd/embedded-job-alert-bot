
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone


def fetch_rss(url, source_name):
    jobs = []

    try:
        response = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0 EmbeddedJobAlertBot/1.0"
            }
        )
        response.raise_for_status()

        root = ET.fromstring(response.content)

        for item in root.findall(".//item"):
            title = item.findtext("title", "")
            link = item.findtext("link", "")
            description = item.findtext("description", "")
            pub_date = item.findtext("pubDate", "")

            if not title or not link:
                continue

            jobs.append({
                "title": title.strip(),
                "link": link.strip(),
                "description": description.strip(),
                "published": pub_date.strip(),
                "source": source_name,
            })

    except Exception as e:
        print(f"[RSS ERROR] {source_name}: {e}")

    return jobs
