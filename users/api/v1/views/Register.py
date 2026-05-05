from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.api.v1.serializers import RegisterSerializer
from users.service import AuthService
from users.exceptions import BaseAppException


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                result = AuthService.register(**serializer.validated_data)
                return Response(result, status=status.HTTP_201_CREATED)

            except BaseAppException as e:
                return Response(e.to_dict(), status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)