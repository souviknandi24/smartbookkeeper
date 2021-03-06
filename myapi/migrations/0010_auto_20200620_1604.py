# Generated by Django 3.0.5 on 2020-06-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_invoice_invoiceitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='bank_account_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='bank_account_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='bank_branch_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='bank_ifs_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='bank_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
