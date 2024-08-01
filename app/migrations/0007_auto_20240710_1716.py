# Generated by Django 3.2.5 on 2024-07-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_pcmax_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcmax',
            name='fst_mail',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='1stメール'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='login_id',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ログインID'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='password',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='パスワード'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='post_content',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='掲示板内容文'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='post_title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='掲示板タイトル'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='return_foot_message',
            field=models.CharField(max_length=400, verbose_name='足跡返し'),
        ),
    ]
