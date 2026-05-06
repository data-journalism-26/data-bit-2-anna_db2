
import requests
import pandas as pd
import time
import random
from players import PLAYERS

def get_pageviews(slug, start="20260401", end="20260430", retries=4):
    url = (
        f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
        f"/en.wikipedia/all-access/all-agents/{slug}/monthly/{start}/{end}"
    )
    headers = {"User-Agent": "WTA-popularity-study/1.0 (student project)"}

    for attempt in range(retries):
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            items = r.json().get("items", [])
            total = sum(i["views"] for i in items)
            monthly = {i["timestamp"][:6]: i["views"] for i in items}
            return total, monthly

results = []

for i, p in enumerate(PLAYERS):
    print(f"[{i+1}/{len(PLAYERS)}] {p['name']}...")
    total, monthly = get_pageviews(p["slug"])

    row = {
        "name":        p["name"],
        "ranking":     p["ranking"],
        "views_total": total,
    }
    row.update({f"views_{k}": v for k, v in monthly.items()})
    results.append(row)


    wait = random.uniform(1.5, 3.5)
    time.sleep(wait)


df = pd.DataFrame(results)

print(df[["name", "ranking", "views_total"]]
      .sort_values("views_total", ascending=False)
      .to_string(index=False))

missing = df[df["views_total"].isna()]

df.to_csv("data/wikipedia_views.csv", index=False)