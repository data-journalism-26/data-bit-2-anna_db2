import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from players import PLAYERS
import time

def scrape_prize_money(slug):
    """Scrape career prize money from Wikipedia"""
    url = f"https://en.wikipedia.org/wiki/{slug.replace('-', '_').title()}"
    # Kilka wariantów nazwy strony
    variants = [
        slug.replace('-', '_').title(),
        slug.replace('-', '_'),
        slug.title().replace('-', '_')
    ]
    
    for variant in variants:
        url = f"https://en.wikipedia.org/wiki/{variant}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200:
            continue
            
        soup = BeautifulSoup(r.text, "html.parser")
        
        
        infobox = soup.find("table", {"class": re.compile("infobox")})
        if not infobox:
            continue
            
        for row in infobox.find_all("tr"):
            header = row.find("th")
            value = row.find("td")
            if header and value:
                if "prize" in header.text.lower():
                   
                    text = value.text.strip()
                    numbers = re.findall(r'[\d,]+', text)
                    if numbers:
                        amount = int(numbers[0].replace(',', ''))
                        return amount
    return None

results = []
for p in PLAYERS:
    print(f"Scraping {p['name']}...")
    prize = scrape_prize_money(p['slug'])
    results.append({"name": p["name"], "prize_money_usd": prize})
    time.sleep(1)

df_prize = pd.DataFrame(results)
print(df_prize)

df_prize.to_csv("data/prize_money.csv", index=False)