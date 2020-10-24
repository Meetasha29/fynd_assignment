from repository.queries.user_perm_mapping_queries import UserPermissionMapping


class UserPermissionManager(object):
    """manager class to create user permission mapping"""

    @staticmethod
    def create(username, permission_code, auto_commit=True):
        create_dict = {
            "permission_code": permission_code,
            "username": username
        }

        user_perm_query_instance = UserPermissionMapping()
        user_perm = user_perm_query_instance.create(create_dict, auto_commit)
        return user_perm
