from users.models import Otp
from django.utils import timezone


class OtpRepository:

    @staticmethod
    def create_otp(user, code: str, expires_at):
        otp = Otp.objects.create(
            user = user,
            otp = code,
            expires_at = expires_at
        )
        return otp

    @staticmethod
    def get_valid(user, code: str):
        otp = Otp.objects.filter(
            user = user,
            otp = code,
            is_used = False,
            expires_at__gte = timezone.now()
        ).first()
        return otp

    @staticmethod
    def mark_used(otp):
        otp.is_used = True
        otp.save()
        return otp

    @staticmethod
    def inactivate_all(user):
        Otp.objects.filter(user=user).update(is_used=True)