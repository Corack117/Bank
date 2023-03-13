from django.db import models
from django.db.models import Q
from django.db.models.functions import Length
from applications.account.models import Account

# Choices
class Status(models.TextChoices):
    SUCCESS = "success"
    PROCESSING = "processing"
    
class Type(models.TextChoices):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

# Create your models here.
class Transaction(models.Model):
    models.CharField.register_lookup(Length)
    
    transaction_id = models.CharField(max_length=20, blank=False, null=False, primary_key = True)
    account_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(blank=False, null=False)
    transaction_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        blank=False, 
        null=False
    )
    description = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        blank=False, 
        null=False
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints =  [
            models.CheckConstraint(
                check=Q(amount__gt=0),
                name='amount_constraint',
                violation_error_message='El monto debe ser mayor a 0'
            ),
            models.CheckConstraint(
                check=Q(status__in=(Status.SUCCESS, Status.PROCESSING)),
                name='transaction_status_constraint',
                violation_error_message='Estatus no valido'
            ),
            models.CheckConstraint(
                check=Q(transaction_type__in=(Type.DEPOSIT, Type.WITHDRAWAL)),
                name='transaction_type_constraint',
                violation_error_message='Estatus no valido'
            ),
            models.CheckConstraint(
                check=Q(transaction_id__length__gte=5) & Q(transaction_id__length__lte=20),
                name='transaction_id_constraint',
                violation_error_message='El ID de transacción debe tener entre 5 a 20 carácteres'
            )
        ]