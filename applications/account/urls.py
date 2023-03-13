from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.API_Accounts.as_view(), name="accounts"),
    path('account', views.API_Account.as_view(), name="account"),
    path('account/<str:pk>', views.API_Account.as_view(), name="account_id")
]