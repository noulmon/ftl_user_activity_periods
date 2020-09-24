from django.core.paginator import Paginator
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserActivityPeriodsView(generics.ListAPIView):
    # user data
    queryset = User.objects.prefetch_related('activity_periods').all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()

            # defining page number and page size
            page_number = request.query_params.get('page_no')
            page_size = request.query_params.get('size', 5)

            paginator = Paginator(queryset, page_size)

            serializer = UserSerializer(paginator.page(page_number), many=True)

            return Response(
                {
                    'ok': False,
                    'members': serializer.data
                }
            )
        except Exception as e:
            return Response(
                {
                    'ok': False,
                    'error': e
                }
            )
