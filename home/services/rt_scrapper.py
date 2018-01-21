import json
from typing import Dict, Optional

import requests
from bs4 import BeautifulSoup


class RTScrapper:
    """Rotten Tomatoes movie data scrapper"""

    REQUEST_TIMEOUT = 5

    @classmethod
    def url_scrapper(cls, url: str) -> Optional[Dict]:
        """Scrapes given urls for json schema"""

        try:
            response = requests.get(url, verify=True, timeout=cls.REQUEST_TIMEOUT)
        except Exception as error:
            # requests can throw few exceptions, so just catch anything for now
            print(error)
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            schema = soup.find('script', attrs={'id': 'jsonLdSchema'})
            return json.loads(schema.text)

    @classmethod
    def movie_scrapper(cls, movie_url: str) -> Optional[Dict]:
        """Scrapes given movie url for json schema and additional elements"""

        try:
            response = requests.get(movie_url, verify=True, timeout=cls.REQUEST_TIMEOUT)
        except Exception as error:
            print(error)
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            schema = soup.find('script', attrs={'id': 'jsonLdSchema'})
            thumbnail = soup.find('img', attrs={'class': 'posterImage'})
            movie_info = soup.find('div', attrs={'class': 'movie_synopsis'})
            json_schema = json.loads(schema.text)
            json_schema['thumbnail'] = thumbnail['src']
            json_schema['movie_info'] = movie_info.text.strip()

            return json_schema

    @staticmethod
    def celeb_scrapper(celeb_url: str) -> None:
        """decided not ti implement because of the lack of time"""
        pass
