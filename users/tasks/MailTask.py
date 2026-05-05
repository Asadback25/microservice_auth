# from celery import shared_task
from django.core.mail import send_mail


# @shared_task
def send_otp_email(email, code):
    send_mail(
        subject="Your OTP Code",
        message=f"Your OTP is: {code}",
        from_email="noreply@yourapp.com",
        recipient_list=[email],
    )