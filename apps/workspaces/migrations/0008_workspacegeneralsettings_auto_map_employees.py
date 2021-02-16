# Generated by Django 3.0.3 on 2021-02-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0007_workspacegeneralsettings_import_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspacegeneralsettings',
            name='auto_map_employees',
            field=models.CharField(help_text='Auto Map Employees type from NetSuite to Fyle', max_length=50, null=True),
        ),
    ]