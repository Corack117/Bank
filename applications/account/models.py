from django.db import models
from django.db.models import Q
from django.db.models.functions import Length

# Choices
class Type(models.TextChoices):
    SAVINGS = "savings"
    CHECKING = "checking"

# Create your models here.
class Account(models.Model):
    models.CharField.register_lookup(Length)
    
    account_number = models.CharField(max_length=20, blank=False, null=False, primary_key = True)
    balance = models.FloatField(blank=False, null=False, default=0)
    customer_name = models.CharField(max_length=150, blank=False, null=False)
    account_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        blank=False, 
        null=False
    )
    account_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints =  [
            models.CheckConstraint(
                check=Q(balance__gte=0),
                name='account_balance_constraint',
                violation_error_message='El balance no puede ser negativo'
            ),
            models.CheckConstraint(
                check=Q(account_number__length__gte=5),
                name='account_number_constraint',
                violation_error_message='El numero de cuenta debe tener entre 5 a 20 carácteres'
            ),
            models.CheckConstraint(
                check=Q(account_type__in=(Type.SAVINGS, Type.CHECKING)),
                name='account_status_constraint',
                violation_error_message='Estatus no valido'
            )
        ]