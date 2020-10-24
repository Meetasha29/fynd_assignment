from sqlalchemy.exc import OperationalError, DBAPIError, TimeoutError, ProgrammingError

from activities.commons.base import ActivityBase
from activities.commons.contexts import MovieCreateContext, MovieListingContext
from activities.validators.movie_exists_validator import MovieExistsValidator
from activities.validators.user_authentication_validator import UserAuthenticationValidator
from activities.validators.user_authorization_validator import UserAuthorizationValidator
from commons.error_codes import DatabaseErrorCodes
from commons.exceptions import ExceptionBase
from commons.error import Error
from repository.managers.movie_manager import MovieManager


class MovieCreationActivity(ActivityBase):
    """
    This activity handles only the creation of the trucks.
    """

    def __init__(self, context_class=MovieCreateContext, validators=None):
        self.validators = validators or {
            'P1': (UserAuthenticationValidator, ),
            'P2': (UserAuthorizationValidator, )
        }
        self.context_class = context_class

        super().__init__()

    def _execute(self):
        """
        This method gets called by the ActivityBase's execute and it consists of actual steps executed for the
        creation the movie. And appends the data objects to the response.

        :return:
        """
        error_code = None
        exception_obj = None

        self.response.message = "Movie Creation Failed"
        try:
            movie = MovieManager.create(name=self.context.name,
                                        director=self.context.director,
                                        imdb_score=self.context.imdb_score,
                                        popularity_99=self.context.popularity_99,
                                        genre=self.context.genre)

            self.response.success = True
            self.response.message = "Movie created Successfully"
            self.response.data.append(movie)

        except OperationalError as e:
            error_code = DatabaseErrorCodes.DB_OPERATIONAL_ERROR
            exception_obj = e
        except ProgrammingError as e:
            error_code = DatabaseErrorCodes.DB_PROGRAMMING_ERROR
            exception_obj = e
        except TimeoutError as e:
            error_code = DatabaseErrorCodes.DB_TIMEOUT_ERROR
            exception_obj = e
        except DBAPIError as e:
            error_code = DatabaseErrorCodes.DB_API_ERROR
            exception_obj = e
        except ExceptionBase as e:
            error_code = e.error_enum
            exception_obj = e

        if error_code and exception_obj:
            self.response.errors.append(Error(error_code.name, error_code.value))


class MovieListingActivity(ActivityBase):
    """
    This activity handles the retrieval and listing of movies
    """
    def __init__(self, context_class=MovieListingContext, validators={}):
        self.context_class = context_class
        self.validators = validators

        super().__init__()

    def _execute(self):
        """
        This method gets called by the ActivityBase's execute and it consists of actual steps executed for the
        listing of the movies. And appends the data objects to the response.
        :return:
        """
        error_code = None
        exception_obj = None

        self.response.message = "Movie Listing Failed"
        try:

            movies = MovieManager.fetch_sorted_movies(name=self.context.name, director=self.context.director)

            self.response.data.extend(movies)
            self.response.success = True
            self.response.message = "Movie Listing successful"
        except OperationalError as e:
            error_code = DatabaseErrorCodes.DB_OPERATIONAL_ERROR
            exception_obj = e
        except ProgrammingError as e:
            error_code = DatabaseErrorCodes.DB_PROGRAMMING_ERROR
            exception_obj = e
        except TimeoutError as e:
            error_code = DatabaseErrorCodes.DB_TIMEOUT_ERROR
            exception_obj = e
        except DBAPIError as e:
            error_code = DatabaseErrorCodes.DB_API_ERROR
            exception_obj = e

        if error_code and exception_obj:
            self.response.errors.append(Error(error_code.name, error_code.value))


class MovieUpdationActivity(ActivityBase):
    """
    This activity handles only the creation of the trucks.
    """

    def __init__(self, context_class=MovieCreateContext, validators=None):
        self.validators = validators or {
            'P1': (UserAuthenticationValidator, ),
            'P2': (UserAuthorizationValidator, ),
            'P3': (MovieExistsValidator, )
        }
        self.context_class = context_class

        super().__init__()

    def _execute(self):
        """
        This method gets called by the ActivityBase's execute and it consists of actual steps executed for the
        updation the movie. And appends the data objects to the response.

        :return:
        """
        error_code = None
        exception_obj = None

        self.response.message = "Movie Updation Failed"
        try:
            movie = MovieManager.update(movie_id=self.context.movie_id,
                                        name=self.context.name,
                                        director=self.context.director,
                                        imdb_score=self.context.imdb_score,
                                        popularity_99=self.context.popularity_99,
                                        genre=self.context.genre)

            self.response.success = True
            self.response.message = "Movie updated Successfully"
            self.response.data.append(movie)

        except OperationalError as e:
            error_code = DatabaseErrorCodes.DB_OPERATIONAL_ERROR
            exception_obj = e
        except ProgrammingError as e:
            error_code = DatabaseErrorCodes.DB_PROGRAMMING_ERROR
            exception_obj = e
        except TimeoutError as e:
            error_code = DatabaseErrorCodes.DB_TIMEOUT_ERROR
            exception_obj = e
        except DBAPIError as e:
            error_code = DatabaseErrorCodes.DB_API_ERROR
            exception_obj = e
        except ExceptionBase as e:
            error_code = e.error_enum
            exception_obj = e

        if error_code and exception_obj:
            self.response.errors.append(Error(error_code.name, error_code.value))


class MovieDeletionActivity(ActivityBase):
    """
    This activity handles only the deletion of the movie.
    """

    def __init__(self, context_class=MovieCreateContext, validators=None):
        self.validators = validators or {
            'P1': (UserAuthenticationValidator, ),
            'P2': (UserAuthorizationValidator, ),
            'P3': (MovieExistsValidator, )
        }
        self.context_class = context_class

        super().__init__()

    def _execute(self):
        """
        This method gets called by the ActivityBase's execute and it consists of actual steps executed for the
        creation the movie. And appends the data objects to the response.

        :return:
        """
        error_code = None
        exception_obj = None

        self.response.message = "Movie Deletion Failed"
        try:
            movie = MovieManager.remove(movie_id=self.context.movie_id)

            self.response.success = True
            self.response.message = "Movie Deleted Successfully"
            self.response.data.append(movie)

        except OperationalError as e:
            error_code = DatabaseErrorCodes.DB_OPERATIONAL_ERROR
            exception_obj = e
        except ProgrammingError as e:
            error_code = DatabaseErrorCodes.DB_PROGRAMMING_ERROR
            exception_obj = e
        except TimeoutError as e:
            error_code = DatabaseErrorCodes.DB_TIMEOUT_ERROR
            exception_obj = e
        except DBAPIError as e:
            error_code = DatabaseErrorCodes.DB_API_ERROR
            exception_obj = e
        except ExceptionBase as e:
            error_code = e.error_enum
            exception_obj = e

        if error_code and exception_obj:
            self.response.errors.append(Error(error_code.name, error_code.value))
