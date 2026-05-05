from users.api.v1.serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.exceptions import BaseAppException
from users.service import AuthService



class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = AuthService.login(**serializer.validated_data)
            return Response(result)

        except BaseAppException as e:
            return Response(e.to_dict(), status=e.status_code)