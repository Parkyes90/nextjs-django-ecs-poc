from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import serializers


class UserListSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField()


@extend_schema(
    responses={200: UserListSerializer},
)
class UserListView(ListAPIView):
    def list(self, request, *args, **kwargs):
        return Response(data=[{"name": 1}])
