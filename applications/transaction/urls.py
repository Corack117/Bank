from django.urls import path
from . import views

urlpatterns = [
    path('transactions/account/<str:pk>', views.API_Transactions_Account.as_view()),
    path('transactions', views.API_Transactions.as_view()),
    path('transaction', views.API_Transaction.as_view()),
    path('transaction/<str:pk>', views.API_Transaction.as_view())
]