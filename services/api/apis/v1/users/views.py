from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class UserListView(ListAPIView):
    def list(self, request, *args, **kwargs):
        return Response(data={'users': ['a', 'b', 'c']})
