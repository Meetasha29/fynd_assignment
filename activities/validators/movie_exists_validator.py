from activities.validators.base import ValidatorBase
from commons.error_codes import ValidationErrorCodes
from commons.exceptions import MovieExistsException
from repository.managers.movie_manager import MovieManager


class MovieExistsValidator(ValidatorBase):
    """Validate if movie exists"""

    def validate(self):
        self.context.movie = MovieManager.fetch_sorted_movies(movie_id=self.context.movie_id)

        if not self.context.movie:
            raise MovieExistsException(ValidationErrorCodes.INVALID_MOVIE)
