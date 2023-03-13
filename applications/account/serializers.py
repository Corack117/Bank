from rest_framework import serializers
from .models import Account, Type
            
class AccountSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('without_fields', None)
        
        super(AccountSerializer, self).__init__(*args, **kwargs)
        
        if fields is not None:
            not_allowed = set(fields)
            for field_name in not_allowed:
                self.fields.pop(field_name)
    
    def validate_account_number(self, value):
        if not (len(value) >= 5 and len(value) <= 20):
            raise serializers.ValidationError("El numero de cuenta debe tener entre 5 a 20 carácteres")
        return value
        
    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("El balance no puede ser negativo")
        return value
    
    def validate_account_type(self, value):
        if not value in dict(Type.choices):
            raise serializers.ValidationError("Estatus no valido")
        return value
    
    class Meta:
        model = Account
        fields = '__all__'