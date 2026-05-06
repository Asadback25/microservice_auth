from rest_framework.views import APIView
from rest_framework.response import Response
from users.service import AuthService
from users.exceptions import BaseAppException

# users/api/v1/views/ResendOtp.py

class ResendOtpView(APIView):
    def post(self, request, username): # username URLdan keladi
        try:
            # Service'ga faqat username uzatamiz
            result = AuthService.resend_otp(username=username)
            return Response(result)

        except BaseAppException as e:
            return Response(e.to_dict(), status=e.status_code)