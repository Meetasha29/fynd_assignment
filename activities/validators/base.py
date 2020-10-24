class ValidatorBase(object):
    """
        Base validator class
        """

    def __init__(self, context):
        """
        Args:
            All required data should be included in context(dict)
            List all required context attributes here.
        Raises:
            List all Raised error here.
        Side-effects:
            List all other changes like context attributes it sets
            upon successful validation
        Returns:
            Should not return anything. Just raise error in case of failure.
        """
        self.context = context

    def validate(self, *args, **kwargs):
        """
        override this method to write validation logic
        :return:
        """
        raise NotImplementedError('Validate not implemented')
