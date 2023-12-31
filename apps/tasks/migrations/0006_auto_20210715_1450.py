# Generated by Django 3.0.3 on 2021-07-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_tasklog_credit_card_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklog',
            name='status',
            field=models.CharField(choices=[('FATAL', 'FATAL'), ('COMPLETE', 'COMPLETE'), ('IN_PROGRESS', 'IN_PROGRESS'), ('FAILED', 'FAILED'), ('ENQUEUED', 'ENQUEUED')], help_text='Task Status', max_length=255),
        ),
        migrations.AlterField(
            model_name='tasklog',
            name='type',
            field=models.CharField(choices=[('CREATING_JOURNAL_ENTRY', 'CREATING_JOURNAL_ENTRY'), ('CREATING_EXPENSE_REPORT', 'CREATING_EXPENSE_REPORT'), ('CREATING_BILL', 'CREATING_BILL'), ('CREATING_VENDOR_PAYMENT', 'CREATING_VENDOR_PAYMENT'), ('FETCHING_EXPENSES', 'FETCHING_EXPENSES'), ('CREATING_CREDIT_CARD_CHARGE', 'CREATING_CREDIT_CARD_CHARGE')], help_text='Task type (FETCH_EXPENSES / CREATE_BILL)', max_length=50),
        ),
    ]
