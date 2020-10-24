from repository.models import Movie
from .base import BaseQueries


class MovieQueries(BaseQueries):
    """
    Encapsulates all the movie model related queries here.
    """
    model = Movie
