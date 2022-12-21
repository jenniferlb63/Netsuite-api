# Generated by Django 3.1.14 on 2022-12-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0028_auto_20221116_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='is_simplify_report_closure_enabled',
            field=models.BooleanField(default=False, help_text='Simplify report closure is enbaled'),
        ),
        migrations.AddField(
            model_name='workspace',
            name='ccc_last_synced_at',
            field=models.DateTimeField(help_text='Datetime when ccc expenses were pulled last', null=True),
        ),
    ]