from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from commerce.pages import CustomPageNumberPagination

from .mixin import SerializerByMethodMixin
from .permissions import ProductPermissionsCustom
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer


class ProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProductPermissionsCustom]

    queryset = Product.objects.all()
    serializer_map = {"GET": ProductSerializer, "POST": ProductDetailSerializer}

    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProductPermissionsCustom]

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
