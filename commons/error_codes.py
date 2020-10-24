import enum


class DatabaseErrorCodes(enum.Enum):
	DB_OPERATIONAL_ERROR = "Operational error while accessing database"
	DB_PROGRAMMING_ERROR = "Programming error raise while accessing database"
	DB_TIMEOUT_ERROR = "Query has been timed out while execution on database"
	DB_API_ERROR = "Some database api error raise while accessing database"


class ValidationErrorCodes(enum.Enum):
	INVALID_MOVIE = "Movie does not exist"
	INVALID_TOKEN = "Invalid Token"
	USER_AUTHORIZATION_FAILED = "User does not the permission"


class PayloadValidationErrorCodes(enum.Enum):
	pattern = {
		"error_code": "INVALID_FORMAT",
		"error_message": "invalid '{field}' format. Ensure that value entered is valid"
	}
	required = {
		"error_code": "REQUIRED_FIELD",
		"error_message": "'{field}' is a mandatory field"
	}
	type = {
		"error_code": "INVALID_VALUE_TYPE",
		"error_message": "'{field}' should be of type {value}"
	}
