# Generated by Django 3.1.14 on 2023-01-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyle', '0022_expense_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensefilter',
            name='custom_field_type',
            field=models.CharField(help_text='Custom field type', max_length=255, null=True),
        ),
    ]
