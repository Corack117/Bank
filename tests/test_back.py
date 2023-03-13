import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from applications.account.serializers import AccountSerializer
from applications.transaction.serializers import TransactionSerializer
from rest_framework import status
    
@pytest.mark.django_db
def test_account_create():
    print()
    print("-----Creación de cuentas-----")
    accounts = [ 
        {
            "account_number": "1234567890",
            "balance": 0,
            "customer_name": "Sergio Ordaz Romero",
            "account_type": "savings"
        },
        {
            "account_number": "0987654321",
            "balance": 0,
            "customer_name": "Enrique Ordaz Romero",
            "account_type": "checking"
        }
    ]
    
    client = APIClient()
    url = reverse('account')
    for account in accounts:
        response = client.post(url, account, format='json')
        print(response.data)
        assert(response.status_code is status.HTTP_200_OK)
        assert(len(response.data) > 0)
    getAccounts()
    print()

@pytest.mark.django_db
def test_account_getAll():
    printSpaces()
    print("-----Obtención de cuentas-----")
    test_account_create()
    client = APIClient()
    url = reverse('accounts')
    response = client.get(url, format='json')
    assert(response.status_code is status.HTTP_200_OK)
    assert(len(response.data) > 0)
    print('-----GET de cuentas-----')
    print(response.data)
    printSpaces()
    
    
@pytest.mark.django_db
def test_account_update():
    printSpaces()
    print('-----Actualización de cuentas-----')
    test_account_create()
    accounts = [ 
        {
            "account_number": "1234567890",
            "balance": 200,
            "customer_name": "Sergio Ordaz Romero",
            "account_type": "checking"
        },
        {
            "account_number": "0987654321",
            "balance": 4000,
            "customer_name": "Enrique Ordaz Romero",
            "account_type": "savings"
        }
    ]
    client = APIClient()
    for account in accounts:
        url = reverse('account_id', kwargs={'pk': account['account_number']})
        response = client.put(url, account, format='json')
        print(response.data)
        assert(response.status_code is status.HTTP_200_OK)
        assert(len(response.data) > 0)
    print('-----Cuentas actualizadas-----')
    getAccounts()
    printSpaces()


@pytest.mark.django_db
def test_account_delete():
    printSpaces()
    print("-----Eliminación de cuentas-----")
    test_account_update()
    account_number =  "1234567890"
    client = APIClient()
    url = reverse('account_id', kwargs={'pk': account_number})
    response = client.delete(url, format='json')
    assert(response.status_code is status.HTTP_200_OK)
    assert(len(response.data) > 0)
    print('-----Cuenta 1234567890 eliminada-----')
    print(response.data)
    print('-----Cuentas actuales-----')
    getAccounts()
    printSpaces()
    
    
@pytest.mark.django_db
def test_transaction_create():
    printSpaces()
    print('-----Creación de transacciones-----')
    test_account_update()
    transactions = [ 
        {
            "transaction_id": "abcdefghijk",
            "account_number": "1234567890",
            "amount": 500.00,
            "transaction_type": "deposit",
            "description": "ATM deposit",
            "status": "success"
        },
        {
            "transaction_id": "ñlkjhgfdsaz",
            "account_number": "0987654321",
            "amount": 3800.00,
            "transaction_type": "withdrawal",
            "description": "ATM withdraw",
            "status": "success"
        }
    ]
    
    client = APIClient()
    url = reverse('transaction')
    for transaction in transactions:
        response = client.post(url, transaction, format='json')
        print(response.data)
        assert(response.status_code is status.HTTP_200_OK)
        assert(len(response.data) > 0)
    getTransactions()
    print()
    print('-----Cuentas afectadas después de transacciones-----')
    getAccounts()
    printSpaces()


@pytest.mark.django_db
def test_transaction_getAll():
    printSpaces()
    print("-----Obtención de cuentas-----")
    test_transaction_create()
    client = APIClient()
    url = reverse('transactions')
    response = client.get(url, format='json')
    assert(response.status_code is status.HTTP_200_OK)
    assert(len(response.data) > 0)
    print()
    print('-----GET de transacciones-----')
    print(response.data)
    printSpaces()        
        
@pytest.mark.django_db
def test_transaction_update():
    printSpaces()
    print('-----Actualización de transacciones-----')
    test_transaction_create()
    transactions = [ 
        {
            "transaction_id": "abcdefghijk",
            "account_number": "1234567890",
            "amount": 100.00,
            "transaction_type": "withdrawal",
            "description": "ATM withdrawal",
            "status": "success"
        },
        {
            "transaction_id": "ñlkjhgfdsaz",
            "account_number": "0987654321",
            "amount": 4000.00,
            "transaction_type": "withdrawal",
            "description": "ATM withdraw",
            "status": "success"
        }
    ]
    client = APIClient()
    for transaction in transactions:
        url = reverse('transaction_id', kwargs={'pk': transaction['transaction_id']})
        response = client.put(url, transaction, format='json')
        print(response.data)
        assert(response.status_code is status.HTTP_200_OK)
        assert(len(response.data) > 0)
    print('-----Transacciones actualizadas-----')
    getTransactions()
    print()
    print('-----Cuentas afectadas después de transacciones-----')
    getAccounts()
    printSpaces()
    
@pytest.mark.django_db
def test_transaction_delete():
    printSpaces()
    print("-----Eliminación de transacciones-----")
    test_transaction_update()
    transaction_id =  "ñlkjhgfdsaz"
    client = APIClient()
    url = reverse('transaction_id', kwargs={'pk': transaction_id})
    response = client.delete(url, format='json')
    assert(response.status_code is status.HTTP_200_OK)
    assert(len(response.data) > 0)
    print('-----Transacción ñlkjhgfdsaz eliminada-----')
    getTransactions()
    print()
    print('-----Cuentas afectadas después de transacciones-----')
    getAccounts()
    printSpaces()
    
def getAccounts():
    client = APIClient()
    url = reverse('accounts')
    response = client.get(url, format='json')
    print(response.data)
    
def getTransactions():
    client = APIClient()
    url = reverse('transactions')
    response = client.get(url, format='json')
    print(response.data)
        
def printSpaces():
    print()
    print()