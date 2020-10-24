from activities.validators.base import ValidatorBase
from commons.error_codes import ValidationErrorCodes
from commons.exceptions import AuthenticationException
from repository.managers.user_manager import UserManager


class UserAuthenticationValidator(ValidatorBase):
    """Validate if user authenticated (Validate the token)"""

    def validate(self):
        self.context.user = UserManager.fetch_sorted_users(auth_token=self.context.auth_token)

        if not self.context.user:
            raise AuthenticationException(ValidationErrorCodes.INVALID_TOKEN)
