from rest_framework import generics
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserActivityPeriodsView(generics.ListAPIView):
    # user data
    queryset = User.objects.prefetch_related('activity_periods').all()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            # serializing data
            data = UserSerializer(queryset, many=True).data
            return Response(
                {
                    'ok': True,
                    'members': data
                }
            )
        except Exception as e:
            return Response(
                {
                    'ok': False,
                    'error': e
                }
            )
