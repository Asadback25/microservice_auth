from users.api.v1.serializers import ResendOtpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.service import AuthService
from users.exceptions import BaseAppException

class ResendOtpView(APIView):

    def post(self, request):
        serializer = ResendOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = AuthService.resend_otp(**serializer.validated_data)
            return Response(result)

        except BaseAppException as e:
            return Response(e.to_dict(), status=e.status_code)