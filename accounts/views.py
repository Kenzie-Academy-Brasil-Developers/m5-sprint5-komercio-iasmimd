from rest_framework import generics
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .models import Account
from .serializers import AccountSerializer, LoginSerializer


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountNewestView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        newest_accounts = self.kwargs["num"]

        return self.queryset.order_by("-date_joined")[0:newest_accounts]


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status.HTTP_200_OK)

        return Response(
            {"detail": "invalid username or password"}, status.HTTP_401_UNAUTHORIZED
        )
