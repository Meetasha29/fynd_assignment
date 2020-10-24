from repository.queries.permission_queries import PermissionQueries


class PermissionManager(object):
    """manager class to create permission"""

    @staticmethod
    def create(permission_name, permission_code, auto_commit=True):
        create_dict = {
            "permission_code": permission_code,
            "permission_name": permission_name
        }

        permission_query_instance = PermissionQueries()
        permission = permission_query_instance.create(create_dict, auto_commit)
        return permission
