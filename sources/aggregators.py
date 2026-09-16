import requests


def fetch_aggregator(url, source_name):
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

        data = response.json()

        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = data.get("jobs", data.get("results", []))
        else:
            items = []

        for item in items:
            if not isinstance(item, dict):
                continue

            title = (
                item.get("title")
                or item.get("name")
                or item.get("job_title")
                or ""
            )

            link = (
                item.get("url")
                or item.get("link")
                or item.get("apply_url")
                or ""
            )

            if not title or not link:
                continue

            jobs.append({
                "title": str(title).strip(),
                "link": str(link).strip(),
                "description": str(
                    item.get("description", "")
                ).strip(),
                "published": str(
                    item.get("published", "")
                    or item.get("date", "")
                    or item.get("created_at", "")
                ).strip(),
                "source": source_name,
            })

    except Exception as e:
        print(f"[AGGREGATOR ERROR] {source_name}: {e}")

    return jobs
