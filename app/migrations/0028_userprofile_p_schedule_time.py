# Generated by Django 5.1 on 2024-11-16 12:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_remove_userprofile_check_mail_happymail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='p_schedule_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, null=True, size=None, verbose_name='PCMAX予約時間'),
        ),
    ]