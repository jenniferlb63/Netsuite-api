# Generated by Django 3.0.3 on 2021-05-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0011_auto_20210318_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspacegeneralsettings',
            name='auto_create_merchants',
            field=models.BooleanField(default=False, help_text='Auto Create Merchants for CC Charges'),
        ),
    ]
