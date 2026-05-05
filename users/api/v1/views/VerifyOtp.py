from users.api.v1.serializers import VerifyOtpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.service import AuthService
from users.exceptions import BaseAppException


class VerifyOtpView(APIView):

    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = AuthService.verify_otp(**serializer.validated_data)
            return Response(result)

        except BaseAppException as e:
            return Response(e.to_dict(), status=e.status_code)