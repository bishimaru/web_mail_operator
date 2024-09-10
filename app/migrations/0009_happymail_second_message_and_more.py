# Generated by Django 5.1 on 2024-09-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_happymail_chara_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='happymail',
            name='second_message',
            field=models.TextField(blank=True, null=True, verbose_name='2stメール'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='check_mail_happymail',
            field=models.BooleanField(default=False, verbose_name='ハッピー新着チェック'),
        ),
        migrations.AlterField(
            model_name='happymail',
            name='chara_image',
            field=models.ImageField(blank=True, null=True, upload_to='chara_images/', verbose_name='送付画像'),
        ),
    ]