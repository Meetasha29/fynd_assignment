from repository.queries.movie_queries import MovieQueries


class MovieManager(object):
    """manager class to create movie"""

    @staticmethod
    def create(name, director=None, imdb_score=None, popularity_99=None, genre=[], auto_commit=True):
        create_dict = {
            "name": name,
            "director": director,
            "imdb_score": imdb_score,
            "popularity_99": popularity_99,
            "genre": genre
        }

        movie_query_instance = MovieQueries()
        movie = movie_query_instance.create(create_dict, auto_commit)
        return movie

    @staticmethod
    def fetch_sorted_movies(movie_id=None, name=None, director=None):
        """
        This method can be used to select/fetch the movies based on the passed filters
        """
        filter_dict = {
            'id': movie_id,
            'name': name,
            'director': director
        }
        movies = MovieQueries().sorted_select(filter_dict)
        return movies

    @staticmethod
    def update(movie_id, name, director=None, imdb_score=None, popularity_99=None, genre=[], auto_commit=True):
        update_dict = {
            "name": name,
            "director": director,
            "imdb_score": imdb_score,
            "popularity_99": popularity_99,
            "genre": genre
        }

        movie_query_instance = MovieQueries()
        movie_query_instance.update(movie_id, update_dict, auto_commit)
        return movie_query_instance.fetch_first({'id': movie_id})

    @staticmethod
    def remove(movie_id):

        movie_query_instance = MovieQueries()
        movie_query_instance.delete(movie_id)
