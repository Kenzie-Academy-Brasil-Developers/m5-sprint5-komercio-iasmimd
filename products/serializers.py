from rest_framework import serializers

from django.shortcuts import get_object_or_404

from accounts.models import Account
from accounts.serializers import AccountSerializer

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "description", "price", "quantity", "is_active", "seller_id"]


class ProductDetailSerializer(serializers.ModelSerializer):
    seller = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "description", "price", "quantity", "is_active", "seller"]
        depth = 1
