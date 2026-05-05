# users/services/auth_service.py

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from users.repository import UserRepositories
from users.repository import OtpRepository
from users.repository import RoleRepository
from users.repository import ProfileRepository

from users.utils import generate_otp, otp_expiry
from users.utils import generate_tokens
from users.tasks import send_otp_email

from users.exceptions import (
    UserAlreadyExists,
    UserNotFound,
    InvalidCredentials,
    UserNotVerified,
    InvalidOTP
)


class AuthService:

    # ========================
    #  PRIVATE METHODS
    # ========================

    @staticmethod
    def _get_user_by_email(email):
        try:
            return UserRepositories.get_by_email(email)
        except ObjectDoesNotExist:
            raise UserNotFound()

    @staticmethod
    def _check_user_exists(email):
        try:
            UserRepositories.get_by_email(email)
            raise UserAlreadyExists()
        except ObjectDoesNotExist:
            return

    @staticmethod
    def _create_user(username, email, password):
        return UserRepositories.create_user(
            username=username,
            email=email,
            password=password
        )

    @staticmethod
    def _create_profile(user):
        return ProfileRepository.create(user)

    @staticmethod
    def _assign_default_role(user):
        role = RoleRepository.get_default_role()
        if role:
            RoleRepository.assign_role(user, role)

    @staticmethod
    def _generate_and_save_otp(user):
        # eski OTP larni o‘chiramiz
        OtpRepository.inactivate_all(user)

        code = generate_otp()
        expires_at = otp_expiry()

        otp = OtpRepository.create_otp(user, code, expires_at)

        return otp

    @staticmethod
    def _send_otp(user, code):
        send_otp_email.delay(user.email, code)

    # ========================
    #     PUBLIC METHODS
    # ========================

    @staticmethod
    @transaction.atomic
    def register(username: str, email: str, password: str):
        # 1. check
        AuthService._check_user_exists(email)

        # 2. create user
        user = AuthService._create_user(username, email, password)

        # 3. profile
        AuthService._create_profile(user)

        # 4. role
        AuthService._assign_default_role(user)

        # 5. otp
        otp = AuthService._generate_and_save_otp(user)

        # 6. send
        AuthService._send_otp(user, otp.otp)

        return {
            "message": "OTP sent",
            "email": user.email
        }

    @staticmethod
    @transaction.atomic
    def verify_otp(email: str, code: str):
        user = AuthService._get_user_by_email(email)

        otp = OtpRepository.get_valid(user, code)

        if not otp:
            raise InvalidOTP()

        # mark used
        OtpRepository.mark_used(otp)

        # activate user
        UserRepositories.update_user(user, is_active=True)

        return {"message": "User verified"}

    @staticmethod
    @transaction.atomic
    def resend_otp(email: str):
        user = AuthService._get_user_by_email(email)

        otp = AuthService._generate_and_save_otp(user)

        AuthService._send_otp(user, otp.otp)

        return {"message": "OTP resent"}

    @staticmethod
    def login(username: str, password: str):
        user = UserRepositories.get_by_username(username)

        if not user:
            raise UserNotFound()

        if not user.check_password(password):
            raise InvalidCredentials()

        if not user.is_active:
            raise UserNotVerified()

        return generate_tokens(user)