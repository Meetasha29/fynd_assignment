import logging


from commons.exceptions import ExceptionBase
from commons.response import Response
from commons.error import Error


logger = logging.getLogger(__name__)


class ActivityBase:
    """
    Base class for all the activities, defining the sequence of execution and controlling the
    validations and response structures.
    """

    def __init__(self):
        """
        Initializing the response and other objects
        Note - If any other attribute is to be added in the instance then override this and call super().__init__()
        """
        self.response = Response()
        self.context = None
        self.payload = {}

    def execute(self, payload={}, **kwargs):
        """
        This method controls the sequential execution of each step for the activity.
        Executing the vadlidations first and then the execute part.

        :param payload: Dictionary consisting of payload present in the request directly passed after serialization
        """
        self.payload = payload
        # sets the self.context attribute by fetching data from the payload dictionary
        self._set_context(payload, **kwargs)

        # validates the payload based on the validators defined above in the tuples
        self._validate()

        # if validations passed then execute the activity and no error is raised by validator
        if not self.response.errors:
            self._execute()

        return self.response

    def _set_context(self, payload, **kwargs):
        """
        Simply sets the context object as per the payload passed to it
        :param payload:
        :return:
        """
        self.context = self.context_class(**payload)

        for name, value in kwargs.items():
            setattr(self.context, name, value)

    def _validate(self):
        """
        Performs the validations for the request as per the validators defined in the class attributes
        :return:
        """
        # list of errors consisting of dictionary with error message and error code
        validator_errors = []

        for priority_validators in self.validators.values():
            for Validator in priority_validators:
                try:
                    Validator(self.context).validate()
                except ExceptionBase as e:
                    validator_errors.append(Error(e.error_code, e.error_message))
                    logger.error(e)

            if validator_errors:
                break

        # update the errors in the response object
        if validator_errors:
            self.response.success = False
            self.response.errors = validator_errors

    def _execute(self):
        """
        This method needs to be implemented in the inherited class only and it will consist of actual
        steps to be performed in the activity.

        And it must also append the data into the response.
        """
        raise NotImplementedError('execute not implemented')
