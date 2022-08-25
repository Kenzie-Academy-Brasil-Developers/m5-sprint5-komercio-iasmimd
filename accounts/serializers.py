from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Account.objects.all(), fields=["username"]
            ),
        ]
        read_only_fields = ("is_active","date_joined", "is_superuser")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class AccountAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "all"
        read_only_fields = ("date_joined", "is_superuser")
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
