# Generated by Django 3.1.14 on 2022-03-10 09:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0023_configuration_skip_cards_mapping'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspaceschedule',
            name='additional_email_options',
            field=models.JSONField(default=list, help_text='Email and Name of person to send email', null=True),
        ),
        migrations.AddField(
            model_name='workspaceschedule',
            name='emails_selected',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), help_text='File IDs', null=True, size=None),
        ),
        migrations.AddField(
            model_name='workspaceschedule',
            name='error_count',
            field=models.IntegerField(help_text='Number of errors in export', null=True),
        ),
    ]
