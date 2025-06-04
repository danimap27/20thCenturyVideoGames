from django.core.management.base import BaseCommand
import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://20thcenturyvideogames.com/"
CATEGORY_MAP = {
    "consoles": 4,
    "computers": 3,
}


class Command(BaseCommand):
    help = "Scrape data from 20thCenturyVideoGames.com"

    def add_arguments(self, parser):
        parser.add_argument(
            "--category",
            choices=CATEGORY_MAP.keys(),
            default="consoles",
            help="Category to scrape",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=5,
            help="Number of systems to fetch",
        )
        parser.add_argument(
            "--output",
            type=Path,
            default=Path("scraped_data.json"),
            help="Where to store JSON data",
        )

    def handle(self, *args, **options):
        category = options["category"]
        tipo = CATEGORY_MAP[category]
        list_url = f"{BASE_URL}index.php?action=listas&tipo={tipo}"
        resp = requests.get(list_url, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        system_links = []
        for a in soup.find_all("a", href=re.compile("vermodelos")):
            name = a.text.strip()
            if not name or "Consolas" in name or name == "Sistema":
                continue
            href = a.get("href")
            if href and all(href != item["href"] for item in system_links):
                system_links.append({"href": href, "name": name})
        data = []
        for link in system_links[: options["limit"]]:
            url = BASE_URL + link["href"]
            self.stdout.write(f"Fetching {url}")
            models = parse_models_page(url)
            for model in models:
                model["system"] = link["name"]
                model["category"] = category
                data.append(model)
        with open(options["output"], "w") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
        self.stdout.write(self.style.SUCCESS(f"Saved {len(data)} entries to {options['output']}"))


def parse_models_page(url: str):
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for box in soup.select("div#cajamodelo"):
        name_tag = box.select_one("h2")
        if not name_tag:
            continue
        name = name_tag.text.strip()
        year_text = box.select_one("div.peque b")
        year = None
        if year_text:
            m = re.search(r"(\d{4})", year_text.text)
            if m:
                year = int(m.group(1))
        desc_tag = box.select_one("section article details p")
        description = desc_tag.text.strip() if desc_tag else ""
        results.append({"name": name, "year": year, "description": description})
    return results
