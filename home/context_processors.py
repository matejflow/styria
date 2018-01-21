from django.core.cache import cache


def top_movies(*options):
    return {'top_movies': cache.get('top_movies', [])}
