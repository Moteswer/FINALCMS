# Generated by Django 4.2.9 on 2024-02-06 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_rename_role_login_role_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='role_id',
            new_name='role',
        ),
    ]
