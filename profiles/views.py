from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProfileSerializer
from .models import UserProfile


class ProfileDetailView(APIView):
    """Detail profile information by 'GET' method"""
    def get(self, request, pk):
        profile = UserProfile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data)


# class UpdateProfileView(APIView):
#     """Update profile info by 'POST' method"""
#     def post(self, request, pk):
#         profile = UserProfile.objects.get(pk=pk)
#         new_profile = UpdateProfileSerializer(instance=profile,
#                                               data=request.data)
#         if new_profile.is_valid():
#             new_profile.save()
#
#             return Response(status=201)
#         return Response(status=404)
