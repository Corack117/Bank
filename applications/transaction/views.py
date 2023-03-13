from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction, Type, Status
from applications.account.models import Account
from .serializers import TransactionSerializer
from applications.account.serializers import AccountSerializer

# Create your views here.
class API_Transactions_Account(APIView):
    def get(self, request, pk=None, format=None):
        account = Account.objects.get(account_number=pk)
        transactions = account.transaction_set.all()
        account = AccountSerializer(account)
        transactions = TransactionSerializer(transactions, many=True)
        data = {
            'account': account.data,
            'transactions': transactions.data
        }
        return Response(data, status=status.HTTP_200_OK)
        
class API_Transactions(APIView):
    queryset = Transaction.objects
    
    def get(self, request, *args, **kwargs):
        transactions = self.queryset.all()
        transactions = TransactionSerializer(transactions, many=True)
        return Response(transactions.data, status=status.HTTP_200_OK)
        
class API_Transaction(APIView):
    queryset = Transaction.objects
     
    def get(self, request, pk=None, format=None):
        if not pk:
            msg = "Petición no valida"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            transaction = self.queryset.get(transaction_id=pk)
            transaction = TransactionSerializer(transaction)
        except:
            return self.error_unknown_account(pk)
        return Response(transaction.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        transaction_request = request.data
        transaction = TransactionSerializer(data = transaction_request)
        if transaction.is_valid(raise_exception=True):
            transaction.save()
        return Response("Transacción registrada correctamente", status=status.HTTP_200_OK)
        
    def put(self, request, pk=None, format=None):
        if not pk:
            msg = "Petición no valida"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            
        try: 
            transaction_request = request.data
            transaction = self.queryset.get(transaction_id=pk)
            transaction = TransactionSerializer(transaction, data=transaction_request, without_fields=['transaction_id'], partial=True)
            if transaction.is_valid(raise_exception=True):
                transaction.save()
        except: 
            return self.error_unknown_account(pk)
        return Response("Se actualizó correctamente la transacción {}".format(pk), status=status.HTTP_200_OK)
        
    def delete(self, request, pk=None, format=None):
        if not pk:
            msg = "Petición no valida"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            
        try: 
            transaction = self.queryset.get(transaction_id=pk)
            account = transaction.account_number
            newBalance = 0
            if transaction.transaction_type == Type.DEPOSIT:
                newBalance = account.balance - transaction.amount
            else:
                newBalance = account.balance + transaction.amount
            dataUpdated = {'balance': newBalance}
            account = AccountSerializer(account, data=dataUpdated, partial=True)
            if account.is_valid(raise_exception=True):
                account.save()
                transaction.delete()
        except: 
            return self.error_unknown_account(pk)
        return Response("Se eliminó correctamente la transacción {}".format(pk), status=status.HTTP_200_OK)
        
    def error_unknown_account(self, pk):
        return Response("Error, no existe la transacción con id {}".format(pk), status=status.HTTP_400_BAD_REQUEST)