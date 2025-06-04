from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = "Scrape a subset of 20thCenturyVideoGames.com"

    def add_arguments(self, parser):
        parser.add_argument('--limit', type=int, default=10, help='Number of items to fetch')

    def handle(self, *args, **options):
        limit = options['limit']
        url = "https://20thcenturyvideogames.com/index.php?action=listas&tipo=4"
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        entries = []
        for link in soup.select('.footer_list a')[:limit]:
            entries.append(link.text.strip())
        for e in entries:
            self.stdout.write(e)
