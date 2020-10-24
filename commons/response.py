from commons.error import Error


class Response(object):
    """
    Plain response object for all the API integrations
    """
    def __init__(self):
        """
        Initializes Response object
        """
        self.data = []
        self.metadata = {}
        self.success = False
        self.errors = []
        self.message = ""

    def to_dict(self):
        """
        Can be used to convert the response to dictionary
        :return: Dictionary representation of the response
        """
        errors = []
        for error in self.errors:
            assert isinstance(error, Error)
            errors.append(error.to_dict())

        data = []
        for each in self.data:
            if each:
                if isinstance(each, dict):
                    data.append(each)
                else:
                    data.append(each.to_dict())
        self.data = data

        return {
            "success": self.success,
            "errors": errors,
            "message": self.message,
            "data": self.data,
            "_metadata": self.metadata
        }
