# Generated by Django 5.1 on 2024-09-28 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_pcmax_gmail_password_alter_pcmax_mail_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcmax',
            name='gmail_password',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Gmailパスワード'),
        ),
    ]
