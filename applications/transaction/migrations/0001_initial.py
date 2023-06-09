# Generated by Django 4.1.7 on 2023-03-12 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('transaction_type', models.CharField(choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')], max_length=20)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('success', 'Success'), ('processing', 'Processing')], max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.AddConstraint(
            model_name='transaction',
            constraint=models.CheckConstraint(check=models.Q(('amount__gt', 0)), name='amount_constraint', violation_error_message='El monto debe ser mayor a 0'),
        ),
        migrations.AddConstraint(
            model_name='transaction',
            constraint=models.CheckConstraint(check=models.Q(('status__in', ('success', 'processing'))), name='transaction_status_constraint', violation_error_message='Estatus no valido'),
        ),
        migrations.AddConstraint(
            model_name='transaction',
            constraint=models.CheckConstraint(check=models.Q(('transaction_type__in', ('deposit', 'withdrawal'))), name='transaction_type_constraint', violation_error_message='Estatus no valido'),
        ),
        migrations.AddConstraint(
            model_name='transaction',
            constraint=models.CheckConstraint(check=models.Q(('transaction_id__length__gte', 5), ('transaction_id__length__lte', 20)), name='transaction_id_constraint', violation_error_message='El ID de transacción debe tener entre 5 a 20 carácteres'),
        ),
    ]
