from users.api.v1.serializers import VerifyOtpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.service import AuthService
from users.exceptions import BaseAppException

class VerifyOtpView(APIView):
    # URL orqali username keladi (masalan: /verify-otp/test1/)
    def post(self, request, username):
        serializer = VerifyOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            # Serializerdan faqat code keladi, username'ni esa URLdan olib qo'shamiz
            result = AuthService.verify_otp(
                username=username,
                **serializer.validated_data
            )
            return Response(result)

        except BaseAppException as e:
            return Response(e.to_dict(), status=e.status_code)