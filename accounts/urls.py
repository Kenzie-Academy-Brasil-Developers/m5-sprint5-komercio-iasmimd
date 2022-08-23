from django.urls import path
from .views import AccountView, AccountNewestView, LoginView

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/newest/<int:num>/", AccountNewestView.as_view()),
    path("login/", LoginView.as_view()),
]
