# Generated by Django 3.1.14 on 2022-11-22 07:50

import apps.fyle.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyle', '0018_expense_corporate_card_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensegroupsettings',
            name='ccc_expense_state',
            field=models.CharField(choices=[('APPROVED', 'APPROVED'), ('PAID', 'PAID')], default=apps.fyle.models.get_default_ccc_expense_state, help_text='state at which the ccc expenses are fetched (APPROVED/PAID)', max_length=100, null=True),
        ),
    ]
