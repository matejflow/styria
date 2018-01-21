from django.db import models

from core.mixins import TimeStampModelMixin


class MovieQuerySet(models.QuerySet):
    pass


class Movie(TimeStampModelMixin):
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.CharField(max_length=256, null=True, blank=True)
    thumbnail = models.CharField(max_length=256, null=True, blank=True)
    production_company = models.CharField(max_length=64)
    rating_content = models.CharField(max_length=16)
    rating_value = models.IntegerField()
    url = models.CharField(max_length=256, unique=True)
    opening_position = models.IntegerField()

    objects = MovieQuerySet.as_manager()

    class Meta:
        db_table = "movies"
