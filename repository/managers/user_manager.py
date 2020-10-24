from repository.queries.user_queries import UserQueries


class UserManager(object):
    """manager class to create user"""

    @staticmethod
    def create(username, password=None, auto_commit=True):
        create_dict = {
            "username": username,
            "password": password
        }

        user_query_instance = UserQueries()
        user = user_query_instance.create(create_dict, auto_commit)
        return user

    @staticmethod
    def fetch_sorted_users(username=None, auth_token=None):
        """
        This method can be used to select/fetch the users based on the passed filters
        """
        filter_dict = {
            'username': username,
            'auth_token': auth_token
        }
        users = UserQueries().sorted_select(filter_dict)
        return users

    @staticmethod
    def update(user_id, auth_token, auto_commit=True):
        update_dict = {
            "auth_token": auth_token
        }

        user_query_instance = UserQueries()
        user_query_instance.update(user_id, update_dict, auto_commit)
        return user_query_instance.fetch_first({'id': user_id})
