from repository.models import UserPermissionMapping
from .base import BaseQueries


class UserPermMapQueries(BaseQueries):
    """handles queries related to UserPermissionMapping model"""

    model = UserPermissionMapping
