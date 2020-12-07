# Generated by Django 3.0.3 on 2020-11-23 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netsuite', '0006_auto_20201123_0644'),
        ('tasks', '0002_tasklog_expense_report_journal_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklog',
            name='vendor_payment',
            field=models.ForeignKey(help_text='Reference to VendorPayment', null=True, on_delete=django.db.models.deletion.PROTECT, to='netsuite.VendorPayment'),
        ),
    ]