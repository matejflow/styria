from typing import Dict, Optional

from django.core.cache import cache

from home.models import Movie

from .rt_scrapper import RTScrapper


class Scrapper:
    """Pretty ugly scrapper, but with given task, good enough

    Better implementation -> url wouldn't be hardcoded
    """

    URL = 'https://www.rottentomatoes.com'

    def __init__(self) -> None:
        self.rt_opening_movies()

    def rt_opening_movies(self) -> None:
        """Scraps rt oppening movies url for json schema"""

        opening_url = self.URL + '/browse/opening'
        movie_schema = RTScrapper.url_scrapper(opening_url)

        if movie_schema:
            movie_list = movie_schema['itemListElement']
            for movie in movie_list:
                self.movie_creator(movie)
            cache.set('top_movies', Movie.objects.order_by('opening_position')[:5])
        else:
            print('Something went wrong')

    @classmethod
    def movie_creator(cls, movie: Dict) -> None:
        """Creates Movie DB object for given movie URL"""

        movie_url = cls.URL + movie['url']
        movie_data = RTScrapper.movie_scrapper(movie_url)

        if movie_data:
            Movie.objects.update_or_create(
                url=cls.url_extractor(movie_data),
                defaults={
                    'name': movie_data['name'],
                    'description': movie_data['movie_info'],
                    'image': cls.image_extractor(movie_data),
                    'thumbnail': movie_data['thumbnail'],
                    'production_company': movie_data['productionCompany']['name'],
                    'rating_content': movie_data['contentRating'],
                    'rating_value': cls.rating_extractor(movie_data),
                    'opening_position': movie['position']
                }
            )

    @staticmethod
    def rating_extractor(movie_data: Dict) -> int:
        """Checks if rating exists in given schema"""

        try:
            return movie_data['aggregateRating']['ratingValue']
        except KeyError:
            return 0

    @staticmethod
    def url_extractor(movie_data: Dict) -> str:
        """Returns last part of scrapped url for our own DB"""

        print(movie_data['url'])  # only done for preview purpose
        url = movie_data['url'].split('/')
        return url[-1]

    @staticmethod
    def image_extractor(movie_data: Dict) -> Optional[str]:
        """Checks if scrapped data has image"""

        no_image_includes = 'poster_default'
        if no_image_includes not in movie_data['image']:
            return movie_data['image']
