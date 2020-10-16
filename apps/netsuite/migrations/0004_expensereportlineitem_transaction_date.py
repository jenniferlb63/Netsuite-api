# Generated by Django 3.0.3 on 2020-10-06 04:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('netsuite', '0003_auto_20200929_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensereportlineitem',
            name='transaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Expense Report transaction date'),
            preserve_default=False,
        ),
    ]