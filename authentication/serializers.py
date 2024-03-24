from rest_framework import serializers
from authentication.models import User
from django.db import IntegrityError, transaction
from django.conf import settings


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("Can't create user")
        return user

    def perform_create(self, validated_data):
        with transaction.atomic(using=self.Meta._db):
            ModelClass = self.Meta.model
            user = ModelClass._default_manager.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
        _db = settings.AUTH_DB_INSTANCE


class UserCreateRealtorSerializer(UserCreateSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_realtor'] = serializers.BooleanField(style={
            'required': True,
            'allow_blank': False
        })

    def validate(self, attrs):
        return super().validate(attrs)