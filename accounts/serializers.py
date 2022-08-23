from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Account


class AccountSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(), message="username already exists"
            )
        ],
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_seller = serializers.BooleanField(default=False)
    date_joined = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
