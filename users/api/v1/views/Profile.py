from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.api.v1.serializers import ProfileSerializer
from users.service import ProfileService
from users.exceptions import BaseAppException


class ProfileView(APIView):

    def get(self, request):
        try:
            profile = ProfileService.get_profile(request.user)
            serializer = ProfileSerializer(profile)

            return Response(serializer.data)

        except BaseAppException as e:
            return Response(e.to_dict(), status=e.status_code)

    def put(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            profile = ProfileService.update_profile(
                request.user,
                serializer.validated_data
            )

            return Response(ProfileSerializer(profile).data)

        except BaseAppException as e:
            return Response(e.to_dict(), status=e.status_code)