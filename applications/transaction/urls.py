from django.urls import path
from . import views

urlpatterns = [
    path('transactions/account/<str:pk>', views.API_Transactions_Account.as_view(), name="transactions_account"),
    path('transactions', views.API_Transactions.as_view(), name="transactions"),
    path('transaction', views.API_Transaction.as_view(), name="transaction"),
    path('transaction/<str:pk>', views.API_Transaction.as_view(), name="transaction_id")
]