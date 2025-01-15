# Generated by Django 5.1.5 on 2025-01-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_rename_sedond_message_ikukuru_second_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='recieve_mailaddress',
            new_name='user_email',
        ),
        migrations.RemoveField(
            model_name='ikukuru',
            name='login_mailaddress',
        ),
        migrations.AddField(
            model_name='ikukuru',
            name='condition_message',
            field=models.TextField(blank=True, null=True, verbose_name='アドレス内1stメール'),
        ),
        migrations.AddField(
            model_name='ikukuru',
            name='gmail_address',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='gmailアドレス'),
        ),
        migrations.AddField(
            model_name='ikukuru',
            name='gmail_password',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Gmailパスワード'),
        ),
        migrations.AddField(
            model_name='ikukuru',
            name='login_mail_address',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ログインメールアドレス'),
        ),
        migrations.AlterField(
            model_name='ikukuru',
            name='password',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ログインパスワード'),
        ),
    ]
