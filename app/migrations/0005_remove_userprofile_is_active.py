# Generated by Django 5.1 on 2024-08-31 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_userprofile_registration_subscribe_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
    ]
