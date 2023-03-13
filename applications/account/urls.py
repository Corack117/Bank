from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.API_Accounts.as_view()),
    path('account', views.API_Account.as_view()),
    path('account/<str:pk>', views.API_Account.as_view())
]