
from .BaseExceptions  import BaseAppException


class UserAlreadyExists(BaseAppException):
    status_code = 400
    default_message = "User already exists"
    default_code = "user_already_exists"


class UserNotFound(BaseAppException):
    status_code = 404
    default_message = "User not found"
    default_code = "user_not_found"


class InvalidCredentials(BaseAppException):
    status_code = 401
    default_message = "Invalid email or password"
    default_code = "invalid_credentials"


class UserNotVerified(BaseAppException):
    status_code = 403
    default_message = "User is not verified"
    default_code = "user_not_verified"


class InvalidOTP(BaseAppException):
    status_code = 400
    default_message = "Invalid or expired OTP"
    default_code = "invalid_otp"