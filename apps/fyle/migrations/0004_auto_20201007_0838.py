# Generated by Django 3.0.3 on 2020-10-07 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fyle', '0003_auto_20200929_1242'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='expensegroup',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='expensegroup',
            name='fyle_group_id',
        ),
    ]