from activities.validators.base import ValidatorBase
from commons.error_codes import ValidationErrorCodes
from commons.exceptions import UserPermissionException


class UserAuthorizationValidator(ValidatorBase):
    """Validate if permission exists for a user"""

    def validate(self):
        permissions = self.context.user[0].permissions
        permission_code = [user_perm.permission_code for user_perm in permissions]
        if self.context.permission_code not in permission_code:
            raise UserPermissionException(ValidationErrorCodes.USER_AUTHORIZATION_FAILED)
