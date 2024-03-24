from django.shortcuts import render
from rest_framework import viewsets, mixins, response, permissions, views
from authentication.serializers import UserCreateSerializer, UserCreateRealtorSerializer, UserGetSerializer
from authentication.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

class UserGetViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserGetSerializer

    def list(self, request, *args, **kwargs):
        queryset = User.objects.get(id=request.user.id)
        serializer = self.get_serializer(queryset)
        return response.Response(serializer.data)



class UserCreateViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserCreateSerializer


class UserCreateRealtorViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserCreateRealtorSerializer