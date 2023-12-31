# Generated by Django 3.1.14 on 2023-02-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netsuite', '0019_auto_20230209_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='reference_number',
            field=models.CharField(help_text='NetSuite reference number', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='creditcardcharge',
            name='reference_number',
            field=models.CharField(help_text='NetSuite reference number', max_length=255, null=True),
        ),
    ]
