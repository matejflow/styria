from django.core.management.base import BaseCommand

from home.services import Scrapper


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        """Fills DB with movies from RT openings"""
        print('SCRAPPING STARTED\n')
        Scrapper()
        print('\nDONE')
