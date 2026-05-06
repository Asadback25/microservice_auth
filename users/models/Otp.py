from django.utils import timezone
from django.db import models
from .User import CustomUser


class Otp(models.Model):
    otp = models.CharField(max_length=6)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username}   -   {self.otp}'

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at