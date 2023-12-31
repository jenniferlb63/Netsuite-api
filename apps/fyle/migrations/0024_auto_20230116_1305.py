# Generated by Django 3.1.14 on 2023-01-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyle', '0023_expensefilter_custom_field_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensefilter',
            name='custom_field_type',
            field=models.CharField(choices=[('SELECT', 'SELECT'), ('NUMBER', 'NUMBER'), ('TEXT', 'TEXT')], help_text='Custom field type', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expensefilter',
            name='join_by',
            field=models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], help_text='Used to join the filter (AND/OR)', max_length=3, null=True),
        ),
    ]
