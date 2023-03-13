from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer

# Create your views here.
class API_Account(APIView):
    queryset = Account.objects
     
    def get(self, request, pk=None, format=None):
        if not pk:
            msg = "Petición no valida"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            account = self.queryset.get(account_number=pk)
            account = AccountSerializer(account)
        except:
            return self.error_unknown_account(pk)
        return Response(account.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        account_request = request.data
        account = AccountSerializer(data = account_request)
        if account.is_valid(raise_exception=True):
            account.save()
        return Response("Cuenta registrada correctamente", status=status.HTTP_200_OK)
        
    def put(self, request, pk=None, format=None):
        if not pk:
            msg = "Petición no valida"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            
        try: 
            account_request = request.data
            account = self.queryset.get(account_number=pk)
            account = AccountSerializer(account, data=account_request, without_fields=['account_number'], partial=True)
            if account.is_valid(raise_exception=True):
                account.save()
        except: 
            return self.error_unknown_account(pk)
        return Response("Se actualizó correctamente la cuenta {}".format(pk), status=status.HTTP_200_OK)
        
    def delete(self, request, pk=None, format=None):
        if not pk:
            msg = "Petición no valida"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            
        try: 
            account = self.queryset.get(account_number=pk)
            account.delete()
        except: 
            return self.error_unknown_account(pk)
        return Response("Se eliminó correctamente la cuenta {}".format(pk), status=status.HTTP_200_OK)
        
    def error_unknown_account(self, pk):
        return Response("Error, no existe la cuenta {}".format(pk), status=status.HTTP_400_BAD_REQUEST)
        
class API_Accounts(APIView):
    queryset = Account.objects
    
    def get(self, request, *args, **kwargs):
        accounts = self.queryset.all()
        accounts = AccountSerializer(accounts, many=True)
        return Response(accounts.data, status=status.HTTP_200_OK)