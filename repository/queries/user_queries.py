from repository.models import User
from .base import BaseQueries


class UserQueries(BaseQueries):
    """
    Encapsulates all the user model related queries here.
    """
    model = User
