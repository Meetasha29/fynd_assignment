from repository.models import Permissions
from .base import BaseQueries


class PermissionQueries(BaseQueries):
    """handles queries related to Permission model"""

    model = Permissions
