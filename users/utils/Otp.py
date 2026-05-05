import random
from datetime import timedelta
from django.utils import timezone


def generate_otp():
    return str(random.randint(100000, 999999))


def otp_expiry(minutes=5):
    return timezone.now() + timedelta(minutes=minutes)