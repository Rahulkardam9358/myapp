from django.shortcuts import render
from rest_framework import viewsets, mixins
from authentication.serializers import UserCreateSerializer, UserCreateRealtorSerializer

# Create your views here.
class UserCreateViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserCreateSerializer


class UserCreateRealtorViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserCreateRealtorSerializer