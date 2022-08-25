from django.urls import path
from .views import AccountView, AccountNewestView, LoginView, AccountDetailView, AdminDetailView

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/newest/<int:num>/", AccountNewestView.as_view()),
    path("login/", LoginView.as_view()),
    path("accounts/<pk>/", AccountDetailView().as_view()),
    path("accounts/<pk>/management/", AdminDetailView().as_view())
]
