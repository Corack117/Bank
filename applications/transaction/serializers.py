from rest_framework import serializers
from .models import Transaction, Type, Status
from applications.account.serializers import AccountSerializer
            
class TransactionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('without_fields', None)
        
        super(TransactionSerializer, self).__init__(*args, **kwargs)
        
        if fields is not None:
            not_allowed = set(fields)
            for field_name in not_allowed:
                self.fields.pop(field_name)
                
    def create(self, validated_data):
        transaction_type = self.initial_data['transaction_type']
        account = validated_data['account_number']
        if transaction_type == Type.DEPOSIT:
            account.balance += self.initial_data['amount']
        elif transaction_type == Type.WITHDRAWAL:
            account.balance -= self.initial_data['amount']
        dataUpdated = {'balance': account.balance}
        account = AccountSerializer(account, dataUpdated, partial=True)
        if account.is_valid(raise_exception=True):
            account = account.save()
        return Transaction.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        account = validated_data.get('account_number')
        transaction_type = validated_data.get('transaction_type')
        newBalance = 0
        if instance.transaction_type == Type.DEPOSIT:
            newBalance = account.balance - instance.amount
        else: 
            newBalance = account.balance + instance.amount
        
        if transaction_type == Type.DEPOSIT:
            newBalance += validated_data['amount']
        else:
            newBalance -= validated_data['amount']
           
        dataUpdated = {'balance': newBalance}
        account = AccountSerializer(account, data=dataUpdated, partial=True)
        if account.is_valid(raise_exception=True):
            account.save()
        instance.transaction_id = validated_data.get('transaction_id', instance.transaction_id)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.transaction_type = validated_data.get('transaction_type', instance.transaction_type)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    
    def validate_transaction_id(self, value):
        if not (len(value) >= 5 and len(value) <= 20):
            raise serializers.ValidationError("El numero de cuenta debe tener entre 5 a 20 carácteres")
        return value
        
    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("El balance no puede ser negativo")
        return value
    
    def validate_transaction_type(self, value):
        if not value in dict(Type.choices):
            raise serializers.ValidationError("Estatus no valido")
        return value
        
    def validate_status(self, value):
        if not value in dict(Status.choices):
            raise serializers.ValidationError("Estatus no valido")
        return value
    
    class Meta:
        model = Transaction
        fields = '__all__'